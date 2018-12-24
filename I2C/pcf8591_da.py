#!/usr/bin/python3
import smbus
import time

bus = smbus.SMBus(1)
add = 0x48

ch0=0x00
ch1=0x01
ch2=0x02
ch3=0x03

def readAD():
	analog = bus.read_byte(add)
	return analog
	
def writeDA(value):
	bus.write_byte_data(add, 0x44, value)

while(0==0):
	for i in range(100, 200):
		time.sleep(0.02)
		print "D/A -> %3d " % (i)	
		writeDA(i)
		
	for i in range(200,100,-1):
		time.sleep(0.02)	
		print "D/A -> %3d " % (i)
		writeDA(i)	
