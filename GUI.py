from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

Window.softinput_mode = "below_target"

# Custom classes implementation
class BackgroundColor(Widget):
	pass
class BackgroundLabel(Label,BackgroundColor):
	pass
class Message(BackgroundLabel):
	pass
class LeftMessage(Message):
	pass
class RightMessage(Message):
	pass
	
class AppLayout(BoxLayout):
	def sendMessage(self):
		txt=self.ids.textbox.text
		if txt:
			msg=LeftMessage(text=txt)
			self.ids.messages.add_widget(msg)
			self.ids.scroller.scroll_to(msg)
			self.ids.textbox.text=''

class ChatApp(App):
        def build(self):
        	self.load_kv('app.kv')
        	return AppLayout()
 
if __name__ == "__main__":
	ChatApp().run()
