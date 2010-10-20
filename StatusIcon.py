import gtk
from System import SystemType

current_system = SystemType()

class StatusIcon:
    def __init__(self, parent):
    
    	self.parent = parent
    
    	iconpath = "WWU.gif"
    
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_file(iconpath)
        self.statusicon.connect("button_press_event", self.click_event)
#	self.statusicon.connect("activate", self.click_event)
        self.statusicon.set_tooltip("WWU wifi")
        
        self.window = gtk.Window()
        self.window.show_all()
        self.window.hide()
        
        self.parent.logged = False
        
    def click_event(self, widget, event):
	if event.button == 1:
		menu = gtk.Menu()

		if self.parent.logged:
			logout = gtk.MenuItem("Logout")
		else:
			login = gtk.MenuItem("Login")

		about = gtk.MenuItem("About")
		quit = gtk.MenuItem("Quit")

		if self.parent.logged:
			logout.connect("activate", self.logout)
		else:
			login.connect("activate", self.login)

		about.connect("activate", self.show_about_dialog)

		if current_system == "linux":
        		quit.connect("activate", self.parent.quit)
		else:
			quit.connect("activate", gtk.main_quit)

		if self.parent.logged:
			menu.append(logout)
		else:
			menu.append(login)

		menu.append(about)
		menu.append(quit)

		menu.show_all()

		menu.popup(None, None, gtk.status_icon_position_menu, event.button, event.time, self.statusicon)
        
    def show_about_dialog(self, widget):
        about_dialog = gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)
        about_dialog.set_name("about wwu-auth")
        about_dialog.set_version("0.1")
        about_dialog.set_authors(["Morgan Borman"])
        		
        about_dialog.run()
        about_dialog.destroy()
        
    def set_visibility(self, visibility):
    	self.statusicon.set_visible(visibility)
    	
    def set_blinking(self, blinking):
    	self.statusicon.set_blinking(blinking)
    	
    def logout(self, opt):
    	self.parent.wwu_de_auth()
    	self.parent.logged = False
    	
    def login(self, opt):
    	self.parent.wwu_auth()
    	self.parent.logged = True
