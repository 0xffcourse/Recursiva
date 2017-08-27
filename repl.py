import itertools
import pygments

from prompt_toolkit.interface import CommandLineInterface
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer, AcceptAction
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import PygmentsStyle, style_from_dict
from prompt_toolkit.shortcuts import print_tokens, create_eventloop, create_prompt_layout
from pygments.token import Token


class RBuffer(Buffer):
    '''Recursiva Buffer isntance that holds cursor position and active document '''
    
    def __init__(self, always_multiline, *args, **kwargs):
        self.always_multiline = always_multiline
        self.return_count = 0
        
        @Condition
        def is_multiline():
            text = self.document.text
            return (
                self.always_multiline and not RBuffer.multiline_evaluator(text)
            )
        super(self.__class__, self).__init__(*args, is_multiline=is_multiline, **kwargs)
    
    def inc(self):
        self.return_count += 1
       
    @staticmethod
    def multiline_evaluator(text):
        text = text.strip()
        return (
            text.endswith(';;') or 
            text in ['quit', 'exit', 'exit()', 'quit()', ':q', 'q']
        )


def key_bindings_registry():
    #binding the registry keys to action for handling reactive state change
    manager = KeyBindingManager()
    registry = manager.registry
    
    
    @registry.add_binding(Keys.ControlQ)
    def _(event):
        event.cli.set_return_value(None)
    
    @registry.add_binding(Keys.Tab)
    def _R(event):
        buff = event.cli.current_buffer
        buff.insert_text(' ' * 4)
    
    @registry.add_binding(Keys.F4)
    def ___(event):
        buff = event.cli.current_buffer
        buff.always_multiline = not buff.always_multiline
    
    return registry


#STYLE
_style = {
    Token: '#ffffff',
    Token.Toolbar: '#ffffff bg:#111111',
    Token.Toolbar.On: '#ffffff',
    Token.Toolbar.Off: '#ffffff',
    Token.Prompt: '#00ff00',
    Token.Continuation: '#00ff00',
    Token.String: '#00ff00'
}

get_style = lambda _name='native': PygmentsStyle.from_defaults(
    style_dict=_style,
    pygments_style_cls=pygments.styles.get_style_by_name(_name)
)

_o_style = style_from_dict({
    Token.OutPrompt: '#9988ff',
    Token.String: '#ffffff'
})

rprint = lambda buff: lambda text:\
        print_tokens(zip(itertools.cycle([Token.OutPrompt, Token.String]),
                         ['Out[%d]: ' % buff.return_count, text, '\n\n']), style=_o_style)

#cli

class RCLI(object):

    def __init__(self):
        self.event_loop = create_eventloop()
        self.cli = None
    
    def __enter__(self):
        self.cli = self._build_cli()
        if self.cli:
            return self.cli
        else:
            raise ValueError('Need to build CLI instance')

    def __exit__(self, *args, **kwargs):
        #print(args, kwargs)
        self.cli = None

    def _build_cli(self):
        

        get_prompt_tokens = lambda cli: \
                            [(Token.Prompt, 'In [%d]: ' % cli.current_buffer.return_count)]
        get_continuation_tokens = lambda cli, width: \
                            [(Token.Continuation, '.' * (width - 1) + ' ')]
        def get_toolbar_tokens(cli):
            result = []
            buff = cli.current_buffer
            text = 'Multiline: ON' if buff.always_multiline else 'Multliline: OFF'
            if buff.always_multiline:
                result.append((Token.Toolbar.On, '[F4] %s' % text))
                result.append((Token.Toolbar.On, '   [*] ";;" to Return'))
            else:
                result.append((Token.Toolbar.Off, '[F4] %s' % text))
            return result

        layout = create_prompt_layout(
            get_prompt_tokens=get_prompt_tokens,
            get_continuation_tokens=get_continuation_tokens,
            get_bottom_toolbar_tokens=get_toolbar_tokens,
            multiline=True
        )

        buffer = RBuffer(
            always_multiline=False,
            accept_action=AcceptAction.RETURN_DOCUMENT
        )
        application = Application(
            layout=layout,
            buffer=buffer,
            style=get_style(),
            key_bindings_registry=key_bindings_registry(),
            ignore_case=True
        )
        render_title = lambda text: zip(itertools.repeat(Token), ['\nRecursiva\n', 'Author: Ayush Ojha | recursiva@fun.gmail.com\n',text,'\n\n'])
        print_tokens(render_title('Version: Experimental '))
        cli = CommandLineInterface(application=application, eventloop=self.event_loop)
        return cli



        








