import gtk

class startupquestion(gtk.Window):
	def __init__(self, parent):
		
		self.objparent = parent
		
		super(startupquestion, self).__init__()
		
		valign = gtk.Alignment(0, 1, 0, 0)
		
		self.vbox = gtk.VBox(False, 3)
		self.vbox.pack_start(valign)
		
		self.question_txt = gtk.Label("Should WWUwifi startup automatically?")
		self.vbox.add(self.question_txt)
		
		self.dontask = gtk.CheckButton(label="Don't ask me again ", use_underline=False)
		if self.objparent.config.read("ask on startup") != None:
			self.dontask.set_active(not self.objparent.config.read("ask on startup"))
		else:
			self.dontask.set_active(False)
		self.dontask.connect("toggled", self.dontasktoggled, None)
		self.vbox.add(self.dontask)
		
		self.h_button_box = gtk.HBox(True, 2)
		
		self.button_yes = gtk.Button("Yes")
	        self.button_yes.connect("clicked", self.yes_startup, None)
	        
		self.button_no = gtk.Button("No")
	        self.button_no.connect("clicked", self.no_startup, None)
	        
	        self.h_button_box.add(self.button_yes)
		self.h_button_box.add(self.button_no)
		
		self.vbox.add(self.h_button_box)
		
		self.add(self.vbox)
		
	def dontasktoggled(self, *args):
		self.objparent.config.write("ask on startup", (not self.dontask.get_active()))
		
	def yes_startup(self, *args):
		self.objparent.config.set_gnome_startup_state(True)
		self.hide_all()
	
	def no_startup(self, *args):
		self.objparent.config.set_gnome_startup_state(False)
		self.hide_all()
		
	def show(self, *args):
		self.show_all()
