import gtk

TIMEOUT = 5000

def check_and_signal():
	#code to check for status of wireless connection goes here
	#should also call main.on_signal
	#signals are as follows
	#0 = Disconnected this may be impractical to use since the timeout is > than most connection timelines
		#maybe possible to reduce timeout depending on how resource draining this function is
	#1 = Connected
	#2 = Connecting
		
def loop():
        gtk.timeout_add (TIMEOUT, check_and_signal)
        gtk.mainloop ()
	return gtk.main()
