#TODO: use keyring
USERNAME = ""
PASSWORD = ""

class CredentialInput:
	def __init__(self):
		valign = gtk.Alignment(0, 1, 0, 0)

		self.window = gtk.Window()

		self.window.set_title("WWUwifi - Credentials")

		self.window.set_size_request(300, 100) 

		self.window.set_position(gtk.WIN_POS_CENTER)

	        self.window.connect("delete_event", self.cancel)
   
        	self.window.connect("destroy", self.cancel)

		self.vbox = gtk.VBox(False, 3)

		self.vbox.pack_start(valign)

		self.h_uname_box = gtk.HBox(True, 2)

		self.uname_txt = gtk.Label("Username:")

		self.h_uname_box.add(self.uname_txt)

		self.username = gtk.Entry(15)

		self.h_uname_box.add(self.username)
		
		self.vbox.add(self.h_uname_box)

		self.h_upass_box = gtk.HBox(True, 2)

		self.upass_txt = gtk.Label("Password:")
		
		self.h_upass_box.add(self.upass_txt)

		self.password = gtk.Entry(15)

		self.password.set_visibility(False)

		self.h_upass_box.add(self.password)

		self.vbox.add(self.h_upass_box)

		self.button = gtk.Button("Submit")

	        self.button.connect("clicked", self.submit, None)

	        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

		self.vbox.add(self.button)
    
	        self.window.add(self.vbox)
    
	        self.window.show_all()

	def cancel(self, *args):
		print args

	def submit(self, *args):
		print args


if __name__ == "__main__":
    import gtk	
    hello = CredentialInput()
    gtk.main()
