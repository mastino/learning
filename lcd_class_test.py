#!/usr/bin/python
#
# testing the LCD class using the raspberry pi's i2c port
# designed for the Grove-LCD JHD1313M1
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful, I accept thanks in the form of 
#    chocolate and introductions to potential employers.

from lcd_class import *
import time
 
r = 1
g = 1
b = 1

lcd = GroveLCD()
lcd.write_string("abcdefghijklmnopqrstuvwxyz1234567890")
lcd.set_rgb(r, g, b)
time.sleep(5) 
lcd.clear()
lcd.write_string(":) :) ;) \nHello World")
lcd.set_rgb(r, g, b)
lcd.return_home()
lcd.write_string(":P")
lcd.move_cursor(0, 9)
lcd.write_string(":D")

lcd.set_display(False)
time.sleep(5) 
lcd.set_display(True)

lcd.set_cursor(False)
time.sleep(5) 
lcd.set_cursor(True)

lcd.set_blink(True)
time.sleep(5) 
lcd.set_blink(False)

lcd.clear()
lcd.set_shift_cursor(False, False)
lcd.move_cursor(0, 10)
lcd.write_string("dlroW")
lcd.return_home()
lcd.set_shift_cursor(False, True)
lcd.write_string("Hello ")
time.sleep(5) 


lcd.clear()
lcd.move_cursor(1, 8)
lcd.write_string(";)")
lcd.move_cursor(0, 15)
lcd.set_shift_cursor(True, True)
str1 = "yo yo what up?"
for c in str1:
   lcd.write_string(c)   
   time.sleep(1)
time.sleep(3) 

lcd.clear()
lcd.move_cursor(0, 0)
lcd.set_shift_cursor(True, False)
str2 = "?u hcum ton ,edud"
# str2 = "dude, not much u?"
for c in str2:
   lcd.write_string(c)
   time.sleep(1)
time.sleep(3) 

lcd.set_shift_cursor(False, True)

# lcd.set_shift_display(True, True)
# # for x in xrange(1,10):
# #    lcd.return_home()
# #    lcd.write_string("abcdefghijklmnopqrstuvwxyz1234567890")
# #    time.sleep(1) 
# lcd.return_home()
# lcd.write_string("abcdefghijklmnopqrstuvwxyz1234567890")
# time.sleep(5) 

# lcd.set_shift_display(False, True)

lcd.clear()
lcd.return_home()
lcd.write_string(":) :) ;) \nHello World")
lcd.set_rgb(r, g, b)
lcd.return_home()
lcd.write_string(":P")
lcd.move_cursor(0, 9)
lcd.write_string(":D")

while 1 == 1:
   #red
   while (r < 255):
      r += 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #yellow
   while (g < 255):
      g += 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #green
   while (r > 1):
      r -= 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #cyan
   while (b < 255):
      b += 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #blue
   while (g > 1):
      g -= 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #purple
   while (r < 255):
      r += 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #white
   while (g < 255):
      g += 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
   #black
   while ( (r > 1) and (g > 1) and (b > 1) ):
      r -= 1
      b -= 1
      g -= 1
      lcd.set_rgb(r, g, b)
      time.sleep(0.002) 
      