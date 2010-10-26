from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["wwuwifi/*.py", "wwuwifi/lin/*.py", "wwuwifi/wwuwifi"]

	

setup(name = "wwuwifi",
	version = "0.15",
	description = "An automatic login utility for WWU campus wireless access points",
	author = "Morgan Borman",
	author_email = "morgan.borman@gmail.com",
	url = "http://github.com/MorganBorman/WWUwifi",
	#Name the folder where your packages live:
	#(If you have other packages (dirs) or modules (py files) then
	#put them into the package directory - they will be found 
	#recursively.)
	packages = ['wwuwifi', "wwuwifi/lin"],
	#'package' package must contain files (see list above)
	#I called the package 'package' thus cleverly confusing the whole issue...
	#This dict maps the package name =to=> directories
	#It says, package *needs* these files.
	package_data = {'wwuwifi' : files },
	data_files=[
		  ('share/applications', ['wwuwifi/data/wwuwifi.desktop']),
		  ('share/pixmaps', ['wwuwifi/data/wwuwifi.png']),
		 ],
	#'wwuwifi' is in the root executable.
	scripts = ["wwuwifi/wwuwifi"],
	long_description = """wwuwifi is a utility to automatically log users into the wifi points around the WWU campus.""",
	#
	classifiers = [
		'Topic :: Utilities',
		'Programming Language :: Python'],
    
) 
