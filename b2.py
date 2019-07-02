#from bluetooth import *
#devices = discover_devices()
#for device in devices:
#    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
# now manually select the desired device or hardcode its name/mac whatever in the script
#bt_addr = '48:27:EA:AD:D5:F7'  
#port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
#s = BluetoothSocket(RFCOMM)
#s.connect((bt_addr, port))

from bluetooth import *
from PyOBEX.client import Client
import sys
from pprint import pprint
devices = discover_devices()
devices
service = find_service(address='48:27:EA:AD:D5:F7')
pprint(service)



addr = "48:27:EA:AD:D5:F7"
print("Searching for OBEX service on %s" % addr)

service_matches = find_service(name=b'OBEX Object Push\x00', address = addr )
if len(service_matches) == 0:
    print("Couldn't find the service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))
client = Client(host, port)
client.connect()
client.put("list_bl.txt", "Hello world\n")
client.disconnect()
