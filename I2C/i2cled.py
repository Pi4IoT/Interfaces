#! /usr/bin/python
#Test vom IC PCF8574TS

import smbus
import sys
import time

bus  = smbus.SMBus(1)

address = 0x20
bus.write_byte(address, 0xff)
pinnummer = [0xff, 0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf]

def set_led(data, zeit):
        bus.write_byte(address, data)
        time.sleep(zeit)
        return


def main():
	while True:
		bus.write_byte(address, 0xff)
		pin_in = ~bus.read_byte(address) 	#Tastenzustand abfragen
												
		print "%x" % (pin_in & 0b10000000)
		
		if pin_in & 0b10000000:
			print "Taste 1 %x" % (pin_in & 0b10000000)
			speed = 0.2
		elif pin_in & 0b01000000:
			print "Taste 2 %x" % (pin_in & 0b01000000)
			speed = 0.01
		else:
			speed = 1	
			
		for pin in pinnummer:
			if pin == 0xff:
				set_led(pin, speed)
			else:
				set_led(pin, 0.05)	


if __name__ == "__main__":
	main()



