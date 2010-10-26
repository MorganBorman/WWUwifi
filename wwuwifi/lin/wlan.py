#TODO: auto detect wireless card(s)
from iwlibs import getNICnames, Wireless

NIC_List = getNICnames()

try:
	wifi = Wireless(NIC_List[0])
except:
	print "Error getting wireless interface."
	quit()
