
from lin.wlan import wifi
#from win.wlan import wifi
#from osx.wlan import wifi
#from loop.wlan import wifi

WWU_PUBLIC_WIFI_SSIDS = ["WWUwireless"]

def getSSID():
	return wifi.getEssid()
	
def is_wwu_wifi():
	return getSSID() in WWU_PUBLIC_WIFI_SSIDS
