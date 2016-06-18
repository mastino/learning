#!/usr/bin/python
#
# running an LCD using the raspberry pi's i2c port
# designed for the Grove-LCD JHD1313M1
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful I accept thanks in the form of 
#    chocolate and introductions to potential employers.

# imports
import smbus
import time

#global objects? and variables
bus = smbus.SMBus(1) # i2c bus
LCD_ADDR = (0x3E>>1) # i2c address for lcd shifted to add R/W bit in smbus func
RGB_ADDR = (0x62>>1) # i2c addr for rgb backlight

