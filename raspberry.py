
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
PORT1 = "/dev/ttyUSB1"
PORT2 = "/dev/ttyUSB2"
# TODO: Replace with the baud rate of your local module.
fieldnames = ["R1","R2","R3"]
BAUD_RATE = 9600
REMOTE_NODE_ID = "Cord1"


def main():
    print(" +-------------+")
    print(" | Calculating |")
    print(" +-------------+\n")

    device= XBeeDevice(PORT, BAUD_RATE)
    device1= XBeeDevice(PORT1, BAUD_RATE)
    device2= XBeeDevice(PORT2, BAUD_RATE)
    
    try:
        device.open()
        device1.open()
        device2.open()
        with open('web/data.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader() 

        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        xbee_network1 = device1.get_network()
        xbee_network2 = device2.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        remote_device1 = xbee_network1.discover_device(REMOTE_NODE_ID)
        remote_device2 = xbee_network2.discover_device(REMOTE_NODE_ID)
        if remote_device and remote_device1 and remote_device2 is None:
            print("Could not find the remote device")
            exit(1)
        while True :    
            # Calculating the rssi of each node from DB rigester in the XBee module .
            device.send_data(remote_device,'a')
            device1.send_data(remote_device1,'c')
            device2.send_data(remote_device2,'b')
            rssi = device.get_parameter("DB")
            rssi1 = device1.get_parameter("DB")
            rssi2 = device2.get_parameter("DB")
            res= int.from_bytes(rssi, byteorder='big')
            res1= int.from_bytes(rssi1, byteorder='big')
            res2= int.from_bytes(rssi2, byteorder='big')
            
            R1=(f"-{res}dbm")
            R2=(f"-{res1}dbm")
            R3=(f"-{res2}dbm")
            with open('web/data.csv', 'a') as outfile:
                csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)

                info = {
                    "R1": res,
                    "R2": res1,
                    "R3": res2
                }

                csv_writer.writerow(info)
            print([R1, R2 ,R3])
            time.sleep(1)
            

    finally:
        if device and device1 and device2 is not None and device.is_open() and device1.is_open() and device2.is_open():
            device.close() and device1.close() and device2.close()
 

if __name__ == '__main__':
    main()