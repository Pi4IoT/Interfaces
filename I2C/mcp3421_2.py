#! /usr/bin/python3
import smbus
import time
from smbus import SMBus

bus  = smbus.SMBus(1)
zeit = 1
while(0==0):
	reading1 = bus.read_i2c_block_data(0x68, 0b00011100) #18 BIT	
	if(reading1[0]&0x80):
		wert= (((reading1[0]^0xff)&0x7f)<<16) +((reading1[1]^0xff)<<8)+(reading1[2]^0xff)
		wert = wert *(-1)
	else:
		wert= ((reading1[0]&0x7f)<<16) +(reading1[1]<<8)+(reading1[2])
	
	wert1 = 1.56*wert/100
	print 'Messwert: %.2f mV' % (wert1)
	time.sleep(zeit)
