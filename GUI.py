from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

Window.softinput_mode = "below_target"

#Palette
# D7D7D7  grey (0.85, 0.85, 0.85, 1)
# F18C8E   red   (0.94, 0.54, 0.55, 1)
# F0B7A4  orange (0.94, 0.71, 0.64, 1)
# F1D1B5  yellow (0.94, 0.82, 0.71, 1)
# 568EA6  blue (0.32, 0.55, 0.65, 1)
# 305F72   black (0.19, 0.37, 0.45, 1)

# Custom classes implementation
class AppChat(BoxLayout):
	pass
class ScreenManager(ScreenManager):
	pass
class MessagesScreen(Screen):
	def sendMessage(self):
		txt=self.ids.textbox.text
		#popup = Popup(title='Test popup', content=Label(text='Hello world'),size_hint=(None, None), size=(600, 800))
		#popup.open()
		if txt:
			msg=SendMessage(text=txt)
			self.ids.messages.add_widget(msg)
			self.ids.scroller.scroll_to(msg)
			self.ids.textbox.text=''

class BackgroundColor(Widget):
	pass
class BackgroundLabel(Label,BackgroundColor):
	pass
class Message(BackgroundLabel):
	pass
	
class SendMessage(Message):
	# Font color
	fnt_r=NumericProperty(0.85)
	fnt_g=NumericProperty(0.85)
	fnt_b=NumericProperty(0.85)
	fnt_a=NumericProperty(1)
	# Background color
	bkg_r=NumericProperty(0.32)
	bkg_g=NumericProperty(0.55)
	bkg_b=NumericProperty(0.65)
	bkg_a=NumericProperty(1)
	
class RecvMessage(Message):
	# Font color
	fnt_r=NumericProperty(0.2)
	fnt_g=NumericProperty(1)
	fnt_b=NumericProperty(1)
	fnt_a=NumericProperty(1)
	# Background color
	bkg_r=NumericProperty(0)
	bkg_g=NumericProperty(0)
	bkg_b=NumericProperty(0)
	bkg_a=NumericProperty(1)
	
class SysMessage(Message):
	# Font color
	fnt_r=NumericProperty(0.5)
	fnt_g=NumericProperty(0.5)
	fnt_b=NumericProperty(0.5)
	fnt_a=NumericProperty(0.5)
	# Background color
	bkg_r=NumericProperty(0)
	bkg_g=NumericProperty(0)
	bkg_b=NumericProperty(0)
	bkg_a=NumericProperty(1)

class SendButton(Button):
	# Font color
	fnt_r=NumericProperty(0.85)
	fnt_g=NumericProperty(0.85)
	fnt_b=NumericProperty(0.85)
	fnt_a=NumericProperty(1)
	# Background color
	bkg_r=NumericProperty(0.94)
	bkg_g=NumericProperty(0.54)
	bkg_b=NumericProperty(0.55)
	bkg_a=NumericProperty(1)

class BackgroundScroller(ScrollView,BackgroundColor):
	# Background color
	bkg_r=NumericProperty(0.94)
	bkg_g=NumericProperty(0.54)
	bkg_b=NumericProperty(0.55)
	bkg_a=NumericProperty(0.3)
	
class ChatApp(App):
        def build(self):
        	self.load_kv('app.kv')
        	return AppChat()
 
if __name__ == "__main__":
	ChatApp().run()
