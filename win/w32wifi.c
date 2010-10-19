#define NOCRYPT
#include "windows.h"
#include "wlanapi.h"
#include <Python.h>



static char *GetSSID()
{
	DWORD serviceVersion = 0;
	HANDLE client = 0;
	DWORD result = 0;

	result = WlanOpenHandle(1, NULL, &serviceVersion, &client);
	if(result != ERROR_SUCCESS) {
		// exit
	}

	// Sanity check.
	if(client == 0) {
		// exit
	}

	PWLAN_INTERFACE_INFO_LIST wlanInterfaceInfoList = 0;
	result = WlanEnumInterfaces(client, 0, &wlanInterfaceInfoList);
	if(result != ERROR_SUCCESS) {
		// Clean up.
		if(client != 0) {
			WlanCloseHandle(client, 0);
			client = 0;
		}
		// This might not be needed.
		if(wlanInterfaceInfoList != 0) {
			WlanFreeMemory(wlanInterfaceInfoList);
			wlanInterfaceInfoList = 0;
		}
		// exit
	}

	PVOID data = 0;
	DWORD size = 0;

	for(unsigned int i = 0; i < wlanInterfaceInfoList->dwNumberOfItems; ++i) {
		result = WlanQueryInterface(
			client, 
			&wlanInterfaceInfoList->InterfaceInfo[i].InterfaceGuid,
			wlan_intf_opcode_current_connection,
			0,
			&size,
			&data,
			0
			);

		if(result != ERROR_SUCCESS) {
			break;
		}

		PWLAN_CONNECTION_ATTRIBUTES wlanConnectionAttributes = 0;
		wlanConnectionAttributes = (PWLAN_CONNECTION_ATTRIBUTES)data;
		if(wlanConnectionAttributes->isState != wlan_interface_state_connected) {
			continue;
		}
	
		char ssidName[33];
		memset(ssidName, 0, 33);

		memcpy(
			ssidName, 
			wlanConnectionAttributes->wlanAssociationAttributes.dot11Ssid.ucSSID,
			wlanConnectionAttributes->wlanAssociationAttributes.dot11Ssid.uSSIDLength);
	
		// ssidName should now contain the SSID name of the first
		// detected interface which is connected. You can store this
		// in a vector or whatever you wish.

		WlanFreeMemory(data);
	}

	if(wlanInterfaceInfoList != 0) {
		WlanFreeMemory(wlanInterfaceInfoList);
	}
	if(client != 0) {
		WlanCloseHandle(client, 0);
	}

	wlanInterfaceInfoList = 0;
	client = 0;
	
	return ssidName;
}

static PyObject *
Get_SSID(PyObject *self, PyObject *args)
{
    const char *ssid;
    
    ssid = GetSSID();
    return Py_BuildValue("s", ssid);
}
