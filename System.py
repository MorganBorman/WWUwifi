import sys
import platform

def SystemType():
	#should return 'win32' on windows and 'linux2' on linux
	return sys.platform()
	
	#returns something like ('Ubuntu', '9.10', 'karmic') on linux
	#platform.dist()
