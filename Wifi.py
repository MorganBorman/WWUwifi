from lin.wlan import wifi

WWU_PUBLIC_WIFI_SSIDS = ["WWUwireless"]

def getSSID():
	return wifi.getEssid()
	
def is_wwu_wifi():
	return getSSID() in WWU_PUBLIC_WIFI_SSIDS
