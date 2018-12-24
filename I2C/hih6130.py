#!/usr/bin/python3

import time
import smbus

from smbus import SMBus

HIH6130 = SMBus(1)

while(True):
	var = [0, 0, 0, 0]

	HIH6130.write_quick(0x27)
	time.sleep(0.050)
	var = HIH6130.read_i2c_block_data(0x27, 0)
	status =(var[0] & 0xc0) >> 6
	humidity = (((var[0] & 0x3f) << 8) + var[1]) * 100.0 / 16382.0
	tempC = ((var[2] << 6) +((var[3] & 0xfc) >> 2)) * 165.0 / 16382.0 - 40.0
	
	print 'Feuchtigkeit: %.2f RH' % humidity
	print 'Temperatur  : %.2f C' % tempC
	time.sleep(1)
