import gobject, dbus
from dbus.mainloop.glib import DBusGMainLoop


#when we get a dbus signal from NetworkManager we need to send the correct state to the main manager
def on_signal(*args):
	if type(args[0]) == dbus.Dictionary:
		if dbus.String(u'State') in args[0].keys():
			if args[0][dbus.String(u'State')] == dbus.UInt32(3):
				#print "connection established"
				main.on_signal(1)
			elif args[0][dbus.String(u'State')] == dbus.UInt32(2):
				#print "connecting..."
				main.on_signal(2)
			elif args[0][dbus.String(u'State')] == dbus.UInt32(4):
				#print "disconnected"
				main.on_signal(0)
				
def loop():
	# dbus events will be part of glib message loop
	DBusGMainLoop(set_as_default=True)
	# attach to D-BUS system bus and wait for DeviceNowActive event
	bus = dbus.SystemBus()
	proxy = bus.get_object('org.freedesktop.NetworkManager',
		'/org/freedesktop/NetworkManager')
	

	proxy.connect_to_signal(None, on_signal)
	# program main loop - waits for events and dispatches handlers
	loop = gobject.MainLoop()
	
	return loop
