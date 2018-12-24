#!/usr/bin/python3
import smbus
from time import sleep

DELAY = 0.5

bus = smbus.SMBus(1)



while(0==0):


	bus.write_i2c_block_data(0x60, 0x12, [0x01])
	#bus.write_byte(0x60, 0x00)	
	sleep(5)
	bus.write_byte(0x60, 0x00)

	reading1 = bus.read_i2c_block_data(0x60, 0x00) 	
	#print('Messung : {} '.format(reading1))
	pressure = ((reading1[0]<<2) +((reading1[1] & 0xc0) >> 6))
	pressure = ((65.0/1023.0) * pressure) + 50
	tempC = (((reading1[2]<<2) +((reading1[3] & 0xc0) >> 6)) -605.75) / -5.35
	print 'Temperature:   : %.1f C  Pressure:   : %.1f kPa' % (tempC,pressure)
	#print("wert: %x %x  - %x %x" % (reading1[0], reading1[1], (reading1[0]<<2), ((reading1[1] & 0xc0) >> 6)))
	
