
from digi.xbee.devices import XBeeDevice
import binascii
import time
# sends simple data 
# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
PORT1 = "/dev/ttyUSB1"
PORT2 = "/dev/ttyUSB2"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = "Hello XBee!"
REMOTE_NODE_ID = "Cord1"


def main():
    print(" +-------------+")
    print(" | Working ..! |")
    print(" +-------------+\n")

    device= XBeeDevice(PORT, BAUD_RATE)
    device1= XBeeDevice(PORT1, BAUD_RATE)
    device2= XBeeDevice(PORT2, BAUD_RATE)
    
    try:
        device.open()
        device1.open()
        device2.open()


        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        xbee_network1 = device1.get_network()
        xbee_network2 = device2.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        remote_device1 = xbee_network1.discover_device(REMOTE_NODE_ID)
        remote_device2 = xbee_network2.discover_device(REMOTE_NODE_ID)
        if remote_device2 is None:
            print("Could not find the remote device")
            exit(1)
        while True :    
            #print("Sending data to %s >> %s..." % (remote_device.get_64bit_addr(), DATA_TO_SEND))
            device.send_data(remote_device, DATA_TO_SEND)
            device1.send_data(remote_device1, DATA_TO_SEND)
            device2.send_data(remote_device2, DATA_TO_SEND)
            rssi = device.get_parameter("DB")
            rssi1 = device1.get_parameter("DB")
            rssi2 = device2.get_parameter("DB")
            res = binascii.hexlify(bytearray(rssi))
            r= int.from_bytes(rssi, byteorder='big')
            r1= int.from_bytes(rssi1, byteorder='big')
            r2= int.from_bytes(rssi2, byteorder='big')
            avg = (r+r1+r2)/3
            print(f"device1= {r}")
            print(f"device2= {r1}")
            print(f"device3= {r2}")
            print(f"avg= {avg}")
            time.sleep(1)
            

    finally:
        if device and device1 and device2 is not None and device.is_open() and device1.is_open() and device2.is_open():
            device2.close() and device.colse() and device1.close()
 

if __name__ == '__main__':
    main()
e A