#!/usr/bin/python
#
# testing the LCD fincutions using the raspberry pi's i2c port
# designed for the Grove-LCD JHD1313M1
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful, I accept thanks in the form of 
#    chocolate and introductions to potential employers.

from lcd import *
import time

lcd_init()
lcd_set_rgb(0, 0, 255)
lcd_write_string("Hello World \n :) :) ;)")
