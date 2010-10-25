#!/usr/bin/env python
# -*- coding: utf-8 -*-

from includes.mechanize import Browser

import StatusIcon
from Wifi import *
import Credentials

from Startup import startupquestion

from Configuration import Configuration

from lin.events import loop

USER_AGENT = "Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.8.1.9) Gecko/20071102 Pardus/2007 Firefox/2.0.0.9"
LOGIN_ADDRESS = "https://wwu.wlan.wwu.edu/fs/customwebauth/login-dmca-focus.html?switch_url=https://wwu.wlan.wwu.edu/login.html&wlan=WWUwireless"

LOGOUT_ADDRESS = "https://wwu.wlan.wwu.edu/logout.html"

def get_title(html):
	return html.split("</title>")[0].split("<title>")[1]
    	

class Manager:
	def __init__(self):
		self.statusicon = StatusIcon.StatusIcon(self)

		self.config = Configuration(self)
		
		self.startup = startupquestion(self)
		if self.config.read("ask on startup") or self.config.read("ask on startup") == None:
			self.startup.show()

		self.CredentialManager = Credentials.CredentialManager(self)

		self.browser = Browser()
		self.browser.addheaders = [("User-agent", USER_AGENT)]

		self.logged = False

		self.check_initial_state()
		self.MainLoop = loop(self)

	#when we get a signal from the wifi event loop we need to do some stuff
	def on_signal(self, state):
		if state == 0:
			#print "disconnected signal"
			self.statusicon.set_visibility(False)
			self.logged = False
		elif state == 1:
			#print "connection established signal"
			self.on_connection()
		elif state == 2:
			#print "acquiring connection signal"
			self.statusicon.set_blinking(True)

	def on_password_change(self):
		#print "our stored password changed"
		if is_wwu_wifi():
			self.statusicon.set_blinking(True)
			if self.wwu_login():
				self.logged = True
				self.statusicon.set_blinking(False)

	def on_connection(self):
		print "on connection"
		self.statusicon.set_blinking(False)
		if is_wwu_wifi():
			print "on wwu wifi"
			self.statusicon.set_visibility(True)
			if self.need_auth():
				print "we need to auth"
				self.statusicon.set_blinking(True)
				if not self.wwu_login():
					print "we failed to auth"
					#tries to log on if it failed this executes
					self.CredentialManager.ask_user()
				else:
					print "we succeeded with auth"
					self.logged = True
					self.statusicon.set_blinking(False)
			else:
				print "we're already logged on"
				self.logged = True
				self.statusicon.set_blinking(False)
		else:
			print "not wwu wifi"
			self.statusicon.set_blinking(False)
			self.statusicon.set_visibility(False)
			self.logged = False
				
	
	def check_initial_state(self):
		#we need to figure out whether we're already on a wifi network
		#and if so whether it's a wwu wireless network
		#and if so whether we need to log on
		
		#this might eventually have some other stuff in it but right now we can
		#just use the on_connection function
		self.on_connection()
		
	def need_auth(self):
		response = self.browser.open("http://www.blankwebpage.com/")
		return get_title(response.read()) == "Web Authentication"

	def wwu_login(self, *args):
		print "logging in..."
		self.statusicon.set_blinking(True)
		self.browser.open(LOGIN_ADDRESS)

		self.browser.select_form("MyForm")

		self.browser.form.set_all_readonly(False)

		self.browser["username"] = self.CredentialManager.get_username()
		self.browser["password"] = self.CredentialManager.get_password() 
		self.browser["buttonClicked"] = "4"
		response = self.browser.submit()
		
		title = get_title(response.read())
		
		self.statusicon.set_blinking(False)
		print "Logged in"
		return title == "Logged In"

	def wwu_logout(self, statusicon="stat"):
		print "logging out..."
		self.statusicon.set_blinking(True)
		
		response = self.browser.open(LOGOUT_ADDRESS)
		
		self.browser.select_form(nr=0)
		self.browser.submit()
		print "Logged out"
		
	def quit(self, statusicon="stat"):
		self.MainLoop.quit()
		
main = Manager()
main.MainLoop.run()
