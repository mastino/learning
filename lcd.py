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
LCD_ADDR = (0x7c>>1) # i2c address for lcd shifted to add R/W bit in smbus func
RGB_ADDR = (0xc4>>1) # i2c addr for rgb backlight
# LCD_ADDR = 0x3E        #alternatively
# RGB_ADDR = 0x62   

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

def lcd_write_string(str):
   num = len(str)
   i = 0
   row = 0
   while( (i < num) && (row < 2) ):
      if( (i == 16) || (i == 32) || (str[i] == "\n") )
         lcd_set_cursor(1, 0)
         row++
      lcd_write_data(ord(str[i++]))


def lcd_set_rgb(r, g, b):
   write_reg(0x00, 0x00)
   write_reg(0x01, 0x00)
   write_reg(0x08, 0xaa)   # set up whatever
   write_reg(0x04, r)      # red
   write_reg(0x03, g)      # green
   write_reg(0x02, b)      # ocre (jk blue)

def lcd_clear():
   lcd_write_cmd(0x01)
   time.sleep(0.002)

def lcd_return_home():
   lcd_write_cmd(0x02)
   time.sleep(0.002)

def lcd_set_cursor(row, col):
   if(row == 0):
      lcd_write_cmd(col | 0x80)
   else:
      lcd_write_cmd(col | 0xc0)
   

def lcd_clear():
   lcd_write_cmd(0x01)
   time.sleep(2)

def lcd_write_cmd(cmd):
   bus.write_byte_data(LCD_ADDR, 0x80, cmd)

def lcd_write_data(data):
   bus.write_byte_data(LCD_ADDR, 0x40, data)

def lcd_write_reg(reg, data):
   bus.write_byte_data(RGB_ADDR, reg, data)
