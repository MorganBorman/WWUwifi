import sys
import platform

def SystemType():
	#should return 'win32' on windows and 'linux2' on linux
	platforms = {'win32': 'windows', 'linux2': 'linux'}
	if sys.platform in platforms:
		return platforms[sys.platform]
	else:
		return 'loop'
	
	#returns something like ('Ubuntu', '9.10', 'karmic') on linux
	#platform.dist()
