import gtk
import gnomekeyring
import glib

APP_NAME = 'WWUwifi'
KEYRING_NAME = 'login'

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
		self.usernamebox.connect("key-press-event", self.on_keypress)
		self.h_uname_box.add(self.usernamebox)
		self.vbox.add(self.h_uname_box)

		self.h_upass_box = gtk.HBox(True, 2)
		self.upass_txt = gtk.Label("Password:")
		self.h_upass_box.add(self.upass_txt)
		self.passwordbox = gtk.Entry(15)
		self.passwordbox.connect("key-press-event", self.on_keypress)
		self.passwordbox.set_visibility(False)
		self.h_upass_box.add(self.passwordbox)

		self.vbox.add(self.h_upass_box)

		self.button = gtk.Button("Submit")
	        self.button.connect("clicked", self.submit, None)
		self.vbox.add(self.button)

	        self.add(self.vbox)
	        
	def on_keypress(self, widget, event):
		keyname = gtk.gdk.keyval_name(event.keyval)
		if keyname == "Return":
			if widget == self.usernamebox:
				self.focus_on_password()
			elif widget == self.passwordbox:
				self.submit()
		elif keyname == "Escape":
			self.cancel()

	def focus_on_password(self, *args):
		self.passwordbox.grab_focus()

	def cancel(self, *args):
		self.canceled = True
		self.hide()
		return True

	def submit(self, *args):
		self.canceled = False
		self.hide()
		self.objparent.cred_changed()
		if self.call_on_submit_function != None:
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
        	glib.set_application_name(APP_NAME)
        	self.objparent = parent
                self.CredDia = CredentialInput(self)
		self.fetch_cred()

	def get_keyring_item(self):
		for id in gnomekeyring.list_item_ids_sync(KEYRING_NAME):
			item = gnomekeyring.item_get_info_sync(KEYRING_NAME, id)
			if item.get_display_name() == 'WWUwifi':
				return item
		return None
		


	def cred_changed(self):
		info = {'Username': self.CredDia.username()}
		gnomekeyring.item_create_sync(KEYRING_NAME, gnomekeyring.ITEM_GENERIC_SECRET, 'WWUwifi', info, self.CredDia.password(), True)

        def get_username(self):
        	gnomekeyring_entry = self.get_keyring_item()
		if gnomekeyring_entry != None:
        		return gnomekeyring_entry.attributes['Username']
	        else:
	        	return ""

	def get_password(self):
		gnomekeyring_entry = self.get_keyring_item()
		if gnomekeyring_entry != None:
	        	return gnomekeyring_entry.get_secret()
	        else:
	        	return ""

	def ask_user(self):
		self.CredDia.call_on_submit(self.objparent.on_password_change)
		self.CredDia.show(self.get_username(), self.get_password())

	def fetch_cred(self):
		gnomekeyring_entry = self.get_keyring_item()
		if gnomekeyring_entry == None:
        		self.CredDia.show("", "")
