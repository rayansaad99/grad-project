# visit https://xbplib.readthedocs.io/en/latest/getting_started_with_xbee_python_library.html#xbee-python-library-software for ref
# visit https://pypi.org/project/rssi/ for ref in rssi
#  1- importing the libarary 
#  2- choosing between Xbeedevice or wifidevice 
#  3-  XBeeDevice is for sending meesseages and stuff 
#  4-  WifiDevice is for sending Data 
#  5-  CellularDevice for remote xbee
#  6- IPprotocol & IPv4Address is for server config
from digi.xbee.devices import XBeeDevice , WiFiDevice , CellularDevice , IPProtocol ,IPv4Address
# using XBeeDevice
device = XBeeDevice("COM1", 9600) # Com replaced with the port ,, 9600 is the baudrate
device.open() #opens the conncetion with the device 
deivce.send_data_broadcast("Hello World!") # broadcast the message 
device.colse() # closes the connection 
# using WiFiDevice 
device2= WiFiDevice("COM",9600) # same as above with modification 
device2.open()
device2.send_ip_data_broadcast(9750, "hello world ") #destination port , Data
device2.colse()
# sending data to remote 
device3= CellularDevice("COM1",9600)
device3.open()
#sending  to server ip with port 11001 using TCP protocol
device3.send_ip_data(IPv4Address("52.43.121.77"), 11001, IPProtocol.TCP, "Hello XBee World!")  
#Read and print the response from the echo server. If response cannot be received, print ERROR.
ip_message = device3.read_ip_data()
print(ip_message.data.decode("utf8") if ip_message is not None else "ERROR")
device3.colse()
