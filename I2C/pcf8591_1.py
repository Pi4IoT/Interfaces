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
	an0 = readAD()
	an1 = readAD()
	an2 = readAD()
	an3 = readAD()
	print "ch0 = %3d  ch1 = %3d  ch2 = %3d  ch3 = %3d  " % (an0, an1, an2, an3)
	writeDA(an0)
	time.sleep(0.5)	
	writeDA(0x00)		
