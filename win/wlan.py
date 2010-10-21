import wmi
c = wmi.WMI()
c = wmi.WMI(namespace="WMI")


class wireless:	
	def getWepStatus(self):
		status = c.MSNdis_80211_WEPStatus()[0].Ndis80211WEPStatus
		return status
		# Ndis80211WEPStatus is 0 when WEP is in use
		# Ndis80211WEPStatus is 2 when over an unsecured connection
		# Ndis80211WEPStatus is 4 when WPA-PSK is in use
		# Ndis80211WEPStatus is 6 when WPA is in use
		# Ndis80211WEPStatus is 7 when disconnected
		
		
	def getEssid(self):
		ssid = ""
		try:
			rawssid = c.MSNdis_80211_ServiceSetIdentifier()[0].Ndis80211Ssid
			length = rawssid[0]
			rawssid = rawssid[4:4+length]

			for byte in rawssid:
				ssid = ssid + chr(byte)
		except:
			print "failed to get ssid"
		return ssid

wifi = wireless()
