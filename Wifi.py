from System import SystemType, systems

current_system = SystemType() 

if current_system == "linux":
	from lin.wlan import wifi
	
elif current_system == "windows":
	from win.wlan import wifi
	
elif current_system == "osx":
	from osx.wlan import wifi
	
elif current_system == "loop":
	from loop.wlan import wifi


WWU_PUBLIC_WIFI_SSIDS = ["WWUwireless", "default"]

def getSSID():
	return wifi.getEssid()
	
def is_wwu_wifi():
	return getSSID() in WWU_PUBLIC_WIFI_SSIDS
