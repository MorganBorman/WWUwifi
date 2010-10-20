#!/usr/bin/env python
# -*- coding: utf-8 -*-

from includes.mechanize import Browser

from StatusIcon import *
from Wifi import *
from Credentials import *
from System import SystemType 

systems = ["linux", "windows", "osx", "loop"]

current_system = SystemType() 

if current_system == "linux":
	from lin.events import loop
	
elif current_system == "windows":
	from win.events import loop
	
elif current_system == "osx":
	from osx.events import loop
	
elif current_system == "loop":
	from loop.events import loop

USER_AGENT = "Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.8.1.9) Gecko/20071102 Pardus/2007 Firefox/2.0.0.9"
LOGIN_ADDRESS = "https://wwu.wlan.wwu.edu/fs/customwebauth/login-dmca-focus.html?switch_url=https://wwu.wlan.wwu.edu/login.html&wlan=WWUwireless"

LOGOUT_ADDRESS = "https://wwu.wlan.wwu.edu/logout.html"

def get_title(html):
	return html.split("</title>")[0].split("<title>")[1]
    	

class manager:
	def __init__(self):
		self.statusicon = StatusIcon(self)

		self.browser = Browser()
		self.browser.addheaders = [("User-agent", USER_AGENT)]
	
		self.check_and_auth()
		self.logged = False
		
		self.MainLoop = loop()

	#when we get a signal from the wifi event loop we need to do some stuff
	def on_signal(self, state):
		if state == 0:
			self.statusicon.set_visibility(False)
			self.logged = False
		elif state == 1:
			#print "connection established"
			self.check_and_auth()
		elif state == 2:
			self.statusicon.set_blinking(True)

				
	def check_and_auth(self):
		self.statusicon.set_blinking(False)
		if is_wwu_wifi():
			self.statusicon.set_visibility(True)
			if self.need_auth():
				self.statusicon.set_blinking(True)
				self.wwu_auth()
				self.statusicon.set_blinking(False)
			self.logged = True
		else:
			self.statusicon.set_visibility(False)
			self.logged = False
		
	def need_auth(self):
		response = self.browser.open("http://www.blankwebpage.com/")
		return get_title(response.read()) == "Web Authentication"

	def wwu_auth(self, statusicon="stat"):
		self.statusicon.set_blinking(True)
		
		self.browser.open(LOGIN_ADDRESS)

		self.browser.select_form("MyForm")

		self.browser.form.set_all_readonly(False)

		self.browser["username"] = USERNAME
		self.browser["password"] = PASSWORD
		self.browser["buttonClicked"] = "4"
		self.browser.submit()
		
		self.statusicon.set_blinking(False)

	def wwu_de_auth(self, statusicon="stat"):
		self.statusicon.set_blinking(True)
		
		response = self.browser.open(LOGOUT_ADDRESS)
		
		self.browser.select_form(nr=0)
		self.browser.submit()
		
	def quit(self, statusicon="stat"):
		self.MainLoop.quit()
		
main = manager()

if current_system == "loop":
	main.MainLoop.run(main)	
else:
	main.MainLoop.run()
