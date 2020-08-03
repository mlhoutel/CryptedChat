import socket
import select 
import sys   
import threading

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

class TextBox(TextInput):
	pass
class MenuLabel(Label):
	pass

class ScreenManager(ScreenManager):
	pass
class MenuScreen(Screen):
	pass
class MessagesScreen(Screen):
	pass

class AppChat(BoxLayout):
	# Server initialisation
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	IP_address="127.0.0.1"
	Port="8027"
	
	def receptThread(self):
		while True:
			sockets_list = [sys.stdin, self.server] 
			read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
			for socks in read_sockets:
				if socks == self.server:
				   	data = socks.recv(2048)
				   	if data:
				   		message = data.decode('utf-8','ignore')
				   		Messages.ids.messages.add_widget(SysMessage(text=message))
				   	else:
				   		self.server.close()
				self.server.close() 
		
	def joinRoom(self):	
		try:
			Menu=self.ids.scr_menu
			Messages=self.ids.scr_messages
			
			self.IP_address=str(Menu.ids.join_ip.text.rstrip())
			self.Port=int(Menu.ids.join_port.text.rstrip())
			
			# Server connection
			self.server.connect((self.IP_address, self.Port)) 
			
			self.ids.sm.transition.direction = 'left'
			self.ids.sm.current = "messages"
			
			Messages.ids.messages.add_widget(SysMessage(text="Connected ("+str(self.IP_address)+":"+str(self.Port)+")"))
			threading.Thread(target=receptThread, args=()).start()
  
		except:
			Menu.ids.join_label.text="Join a room (Can't reach "+str(self.IP_address)+":"+str(self.Port)+")"
			
	def createRoom(self):
		self.ids.sm.transition.direction = 'left'
		self.ids.sm.current = "messages"
	
	def sendMessage(self):
		Menu=self.ids.scr_menu
		Messages=self.ids.scr_messages
		
		txt=Messages.ids.textbox.text.rstrip()
		#popup = Popup(title='Test popup', content=Label(text='Hello world'),size_hint=(None, None), size=(600, 800))
		#popup.open()
		if txt:
			msg=SendMessage(text=txt)
			Messages.ids.messages.add_widget(msg)
			self.server.sendall(txt.encode('utf-8'))
			Messages.ids.scroller.scroll_to(msg)
			Messages.ids.textbox.text=""
			
	def disconnectServer(self):
		self.server.close()
		self.ids.sm.transition.direction = 'right'
		self.ids.sm.current = "menu"
			
class ChatApp(App):
        def build(self):
        	self.load_kv('app.kv')
        	return AppChat()
 
if __name__ == "__main__":
	ChatApp().run()