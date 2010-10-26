from wwuwifi.lin.wlan import wifi

WWU_PUBLIC_WIFI_SSIDS = ["WWUwireless", "default"]

def getSSID():
	return wifi.getEssid()
	
def is_wwu_wifi():
	return getSSID() in WWU_PUBLIC_WIFI_SSIDS
