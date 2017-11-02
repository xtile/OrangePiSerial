#apt-get install python-pip
#pip install pyserial
import serial
import time

ser = serial.Serial(port = "/dev/ttyS2", baudrate=9600) # UART2_RX / PA01 / GPIO1,   UART2_TX / PA00 / GPIO0
ser.close()
ser.open()

while(1):
    if ser.isOpen():
        time.sleep(1)
        if (ser.inWaiting()>0):
            data_str = ser.read(ser.inWaiting()).decode()
            print "Data received = " + str(data_str)