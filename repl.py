import itertools

from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding.manager import KeyBindingManager
from prompt_toolkit.keys import Keys

class RBuffer(Buffer):
	
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




