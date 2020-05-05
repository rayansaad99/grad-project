##############################################
#                                            #
#    auth : Rayan                            #
#    project : Graduation Project            #
#    function : calculate the rssi of a node #
#                                            #
##############################################


from digi.xbee.devices import XBeeDevice
import time
import csv

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB0"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

REMOTE_NODE_ID = "RR"


def main():
    print(" +-------------+")
    print(" | Calculating ..! |")
    print(" +-------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()
        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)
        while True :    
            device.send_data(remote_device,'a')
            rssi = device.get_parameter("DB")
            r= int.from_bytes(rssi, byteorder='big')
            res = (f"-{r}dbm")
            with open('web/data.csv', 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([res])
            print(res)
            
            time.sleep(0.2)
            

    finally:
        if device is not None and device.is_open():
            device.close()
 

if __name__ == '__main__':
    main()