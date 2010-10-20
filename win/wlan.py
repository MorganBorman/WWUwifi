import wmi
c = wmi.WMI()
c = wmi.WMI(namespace="WMI")


class wireless:	
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