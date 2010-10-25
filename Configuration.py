import pickle
import os
import shutil

FILENAME = "~/.WWUwifi.conf"
FILENAME = os.path.expanduser(FILENAME)
STARTUP_FILENAME = "WWUwifi.desktop"
STARTUP_DIRECTORY = "~/.config/autostart/"
STARTUP_DIRECTORY = os.path.expanduser(STARTUP_DIRECTORY)
STARTUP_PATH = STARTUP_DIRECTORY + STARTUP_FILENAME

STARTUP_CONTENTS = """
[Desktop Entry]
Type=Application
Exec=/usr/bin/WWUwifi
Icon=WWUwifi.svg
Hidden=false
NoDisplay=false
Name=WWUwifi
Comment=Login automation for wwu wireless points
X-GNOME-Autostart-enabled="""

class Configuration:
	def __init__(self, parent):
		self.config_values = {}
		if os.path.exists(FILENAME):
			filehandle = open(FILENAME, 'r')
			self.config_values = pickle.load(filehandle)
			filehandle.close()
	
	def write(self, key, value):
		#try:
		filehandle = open(FILENAME, 'w')
		self.config_values[key] = value
		pickle.dump(self.config_values, filehandle)
		filehandle.close()
		return True
		#except:
		#	return False
		
	def read(self, key):
		try:
			return self.config_values[key]
		except:
			return None
		
	def gnome_startup_state(self):
		#returns True if the WWUwifi.desktop has true for autostart
		if os.path.exists(STARTUP_PATH):
			filehandle = open(STARTUP_PATH, 'r')
			lines = filehandle.readlines()
			filehandle.close()
			return lines[-1].split("=", 1)[1] == "true\n" or lines[-1].split("=", 1)[1] == "true"
		else:
			return False
		
	def set_gnome_startup_state(self, state):
		if self.gnome_startup_state() != state:
			filehandle = open(STARTUP_PATH, 'w')
			if state == True:
				filehandle.write(STARTUP_CONTENTS + "true")
			else:
				filehandle.write(STARTUP_CONTENTS + "false")
			filehandle.close()
				
