import gtk

class CredentialInput(gtk.Window):
	def __init__(self, parent):
		self.canceled = True
		self.call_on_submit_function = None
		
		self.objparent = parent
		super(CredentialInput, self).__init__()
		
		valign = gtk.Alignment(0, 1, 0, 0)
		self.set_title("WWUwifi - Credentials")
		self.set_size_request(300, 100) 
		self.set_position(gtk.WIN_POS_CENTER)

	        self.connect("delete_event", self.cancel)
        	self.connect("destroy", self.cancel)

		self.vbox = gtk.VBox(False, 3)
		self.vbox.pack_start(valign)

		self.h_uname_box = gtk.HBox(True, 2)
		self.uname_txt = gtk.Label("Username:")
		self.h_uname_box.add(self.uname_txt)
		self.usernamebox = gtk.Entry(15)
		self.h_uname_box.add(self.usernamebox)
		self.vbox.add(self.h_uname_box)

		self.h_upass_box = gtk.HBox(True, 2)
		self.upass_txt = gtk.Label("Password:")
		self.h_upass_box.add(self.upass_txt)
		self.passwordbox = gtk.Entry(15)
		self.passwordbox.set_visibility(False)
		self.h_upass_box.add(self.passwordbox)

		self.vbox.add(self.h_upass_box)

		self.button = gtk.Button("Submit")
	        self.button.connect("clicked", self.submit, None)
		self.vbox.add(self.button)

	        self.add(self.vbox)

	def cancel(self, *args):
		self.canceled = True
		self.hide()
		self.call_on_exit_function()
		return True

	def submit(self, *args):
		self.canceled = False
		self.hide()
		self.objparent.cred_changed()
		self.call_on_submit_function()
		return True
	
	def show(self, username, password):
		self.usernamebox.set_text(username)
		self.passwordbox.set_text(password)
		self.show_all()
		
	def call_on_submit(self, function):
		self.call_on_submit_function = function

	def hide(self):
		self.hide_all()

	def password(self):
		return self.passwordbox.get_text()

	def username(self):
		return self.usernamebox.get_text()

class CredentialManager:
        def __init__(self, parent):
        	self.objparent = parent
		self.Username = ""
		self.Password = ""
		self.fetch_cred()
                self.CredDia = CredentialInput(self)

	def cred_changed(self):
		self.Username = self.CredDia.password()
		self.Password = self.CredDia.username()

        def get_username(self):
		return self.Username

	def get_password(self):
		return self.Password

	def ask_user(self):
		self.CredDia.call_on_submit(self.objparent.on_password_change)
		self.CredDia.show(self.Username, self.Password)

	def fetch_cred(self):
		self.Username = ""
		self.Password = ""

if __name__ == "__main__":
    hello = CredentialInput()
    gtk.main()
