import time
import threading

class pollingLoop( threading.Thread ):
	def __init__(self):
		pass
	
	def run(self, main):
		while 1:
			time.sleep(15)
			print "sending signal: disconnected"
			main.on_signal(0)
			time.sleep(15)
			print "sending signal: aquiring connection"
			main.on_signal(1)
			time.sleep(15)
			print "sending signal: connected"
			main.on_signal(2)
			
				
def loop():
	loop = pollingLoop()
	
	return loop
