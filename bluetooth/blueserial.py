#! /usr/bin/python
import serial
import time

bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=115200)
print("Bluetooth connected")
try:
	while 1:
		data = bluetoothSerial.readline()
		print(data)
		time.sleep(1)
		bluetoothSerial.write(data)
		
except KeyboardInterrupt:
	print("Quit")
