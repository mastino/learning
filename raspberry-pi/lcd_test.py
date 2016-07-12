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
 
r = 1
g = 1
b = 1

lcd_init()
lcd_write_string("abcdefghijklmnopqrstuvwxyz1234567890")
lcd_set_rgb(r, g, b)
time.sleep(5) 
lcd_clear()
lcd_write_string(":) :) ;) \nHello World")
lcd_set_rgb(r, g, b)
lcd_return_home()
lcd_write_string(":P")
lcd_set_cursor(0, 9)
lcd_write_string(":D")
time.sleep(0.002) 
while 1 == 1:
   #red
   while (r < 255):
      r += 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #yellow
   while (g < 255):
      g += 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #green
   while (r > 1):
      r -= 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #cyan
   while (b < 255):
      b += 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #blue
   while (g > 1):
      g -= 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #purple
   while (r < 255):
      r += 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #white
   while (g < 255):
      g += 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
   #black
   while ( (r > 1) and (g > 1) and (b > 1) ):
      r -= 1
      b -= 1
      g -= 1
      lcd_set_rgb(r, g, b)
      time.sleep(0.002) 
      