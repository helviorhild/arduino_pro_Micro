#!/usr/bin/python3
#!/usr/bin/env python
import time
import serial, sys,os
serialPort ='/dev/ttyACM0'
#serialPort = sys.argv[1]
print (serialPort)

ser = serial.Serial(
    port=serialPort,
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.setRTS(True)
ser.setDTR(False)

ser.isOpen()
ser.close()  
comando='avrdude -v -v -v -patmega32u4 -cavr109 -P' + serialPort+ ' -b57600 -D -Uflash:w:'+sys.argv[1]+':i'
time.sleep(1)
os.system(comando) 