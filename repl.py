import itertools
import pygments

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys
from prompt_tooklit.styles import PygmentsStyle, style_from_dict
from prompt_toolkit.shortcuts import print_tokens
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
				self.always_multiline or not RBuffer.multiline_evaluator(text)
			)
		super(self.__class__, self).__init__(*args, is_multiline=is_multiline, **kwargs)
		
		@staticmethod
		def multiline_evaluator(text):
			text = text.strip()
			return (
				text.endswith(';;') or 
				text in ['quit', 'exit', 'exit()', 'quit()', ':q', 'q']
			)


def key_bindings_registry():
	#binding the registry keys to action for handling reactive state change
	manager = KeyBindingManger()
	registry = manager.registry
	
	@registry.add_binding(Keys.ControlQ)
	def _(event):
		event.cli.set_return_value(None)
	
	@registry.add_binding(Keys.Tab)
	def __(event):
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
	Token.Toolbar.On: '#666666',
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

rprint = lambda count, text:\
		print_tokens(zip(itertools.cycle([Token.OutPrompt, Token.String]),
										['Out[%d]: ' % count, text, '\n\n']), style=_o_style)










