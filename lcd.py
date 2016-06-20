#!/usr/bin/python
#
# running an LCD using the raspberry pi's i2c port
# designed for the Grove-LCD JHD1313M1
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful, I accept thanks in the form of 
#    chocolate and introductions to potential employers.

# imports
import smbus
import time

#global objects? and variables
bus = smbus.SMBus(1) # i2c bus
LCD_ADDR = (0x3E>>1) # i2c address for lcd shifted to add R/W bit in smbus func
RGB_ADDR = (0x62>>1) # i2c addr for rgb backlight

def lcd_init():
  # Initialise display
  time.sleep(0.05)      # wait after power on
  lcd_write_cmd(0x38)   # 2 lines (bit 3) display on (bit 2)
  time.sleep(0.001)     # 
  lcd_write_cmd(0x0E)   # cursor on (bit 1) blink off (bit 0)
  time.sleep(0.001)     # 
  lcd_write_cmd(0x01)   # clear display
  time.sleep(0.001)     # 
  lcd_write_cmd(0x07)   # increment (bit 1) entire shift (bit 0)
  time.sleep(0.002)     # 


def lcd_write_cmd(cmd):
   bus.write_byte(LCD_ADDR, 0x80)
   bus.write_byte(LCD_ADDR, cmd)

def lcd_write_data(data):
   bus.write_byte(LCD_ADDR, 0x40)
   bus.write_byte(LCD_ADDR, data)