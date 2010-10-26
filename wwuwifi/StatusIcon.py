import gtk

class StatusIcon:
    def __init__(self, parent):
    
    	self.parent = parent
    
    	iconpath = "/usr/share/pixmaps/wwuwifi.png"
    
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_file(iconpath)
        self.statusicon.connect("button_press_event", self.click_event)
#	self.statusicon.connect("activate", self.click_event)
        self.statusicon.set_tooltip("WWUwifi")
        
        self.window = gtk.Window()
        self.window.show_all()
        self.window.hide()
        
    def click_event(self, widget, event):
	if event.button == 1:
		menu = gtk.Menu()
		
		config_menu = gtk.Menu()
		startup = gtk.MenuItem("Startup")
		startup.connect("activate", self.parent.startup.show)
		credentials = gtk.MenuItem("Credentials")
		credentials.connect("activate", self.parent.CredentialManager.ask_user)
		config_menu.append(startup)
		config_menu.append(credentials)
		
		config = gtk.MenuItem("Config")
		config.set_submenu(config_menu)

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

        	quit.connect("activate", self.parent.quit)

		if self.parent.logged:
			menu.append(logout)
		else:
			menu.append(login)
			
		menu.append(config)

		menu.append(about)
		menu.append(quit)

		menu.show_all()

		menu.popup(None, None, gtk.status_icon_position_menu, event.button, event.time, self.statusicon)
        
    def show_about_dialog(self, widget):
        about_dialog = gtk.AboutDialog()

        about_dialog.set_destroy_with_parent(True)
        about_dialog.set_name("WWUwifi auto-login")
        about_dialog.set_version("0.15 - ubuntu")
        about_dialog.set_authors(["Morgan Borman"])
        		
        about_dialog.run()
        about_dialog.destroy()
        
    def set_visibility(self, visibility):
    	self.statusicon.set_visible(visibility)
    	
    def set_blinking(self, blinking):
    	self.statusicon.set_blinking(blinking)
    	
    def logout(self, opt):
    	self.parent.wwu_logout()
    	self.parent.logged = False
    	
    def login(self, opt):
    	self.parent.wwu_login()
