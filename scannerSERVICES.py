import bluetooth  
import lightblue  

# we should know  
target_name = "Galaxy S8"
   
# we don't know yet  
obex_port = None                 
target_address = None  
   
print("searching for nearby devices...")
nearby_devices = bluetooth.discover_devices()  
   
for bdaddr in nearby_devices:  
  print(bluetooth.lookup_name( bdaddr ))
  if target_name == bluetooth.lookup_name( bdaddr ):  
    print("found the target device!")
    target_address = bdaddr  
    break  
   
print("searching for the object push service...")
print('Port       Service')
services = lightblue.findservices(target_address)  
for service in services:
    print(str(service[1]) + '           ' + str(service[2]))
