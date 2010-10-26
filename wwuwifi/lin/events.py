import gobject, dbus
from dbus.mainloop.glib import DBusGMainLoop


class loop:
	def __init__(self, parent):
		self.parent = parent
		
		# dbus events will be part of glib message loop
		DBusGMainLoop(set_as_default=True)
		# attach to D-BUS system bus and wait for DeviceNowActive event
		bus = dbus.SystemBus()
		proxy = bus.get_object('org.freedesktop.NetworkManager',
			'/org/freedesktop/NetworkManager')
	

		proxy.connect_to_signal(None, self.on_signal)
		# program main loop - waits for events and dispatches handlers
		self.loop = gobject.MainLoop()

	#when we get a dbus signal from NetworkManager we need to send the correct state to the main manager
	def on_signal(self, *args):
		if type(args[0]) == dbus.Dictionary:
			if dbus.String(u'State') in args[0].keys():
				if args[0][dbus.String(u'State')] == dbus.UInt32(3):
					#print "connection established"
					self.parent.on_signal(1)
				elif args[0][dbus.String(u'State')] == dbus.UInt32(2):
					#print "connecting..."
					self.parent.on_signal(2)
				elif args[0][dbus.String(u'State')] == dbus.UInt32(4):
					#print "disconnected"
					self.parent.on_signal(0)

		
	def run(self):
		self.loop.run()
		
	def quit(self):
		self.loop.quit()
