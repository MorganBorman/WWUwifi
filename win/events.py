import gtk
import glib
from wlan import wifi

TIMEOUT = 1000

class event_system:
	def __init__(self, parent):
		self.parent = parent
		self.previous_status = -1
		self.build_loop()
		
	def check_and_signal(self):
		#code to check for status of wireless connection goes here
		#should also call main.on_signal
		#signals are as follows
		#0 = Disconnected 
		#1 = Connected
		#2 = Connecting doesn't seem to be a wmi way to determine this
		#print "here's an iteration of check_and_signal"
		status = wifi.getWepStatus()
		if status != self.previous_status:
			if status == 0 or status == 2 or status == 4 or status == 6:
				self.parent.on_signal(1)
			elif status == 7:
				self.parent.on_signal(0)
			self.previous_status = status
		return True
			
	def build_loop(self):
		glib.timeout_add(TIMEOUT, self.check_and_signal)
		gtk.main()
		#gtk.timeout_add (TIMEOUT, self.check_and_signal)

def loop(parent):
	return event_system(parent)