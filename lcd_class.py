#!/usr/bin/python
#
# running an LCD using the raspberry pi's i2c port
# designed for the Grove-LCD JHD1313M1
# class instead of stand alone functions provides more flexibility
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful, I accept thanks in the form of 
#    chocolate and introductions to potential employers.
#
# The following were heavily referenced and both use the MIT license:
# https://github.com/DexterInd/GrovePi/tree/master/Software/Python/grove_rgb_lcd
# https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight

# imports
import smbus
import time

class GroveLCD:

  bus = smbus.SMBus(1) # i2c bus
  LCD_ADDR = (0x7c>>1) # i2c address for lcd shifted to add R/W bit in smbus func
  RGB_ADDR = (0xc4>>1) # i2c addr for rgb backlight
  # These addresses are always the same it seems, even if we plug in more than one
  #   This is a wierd thing I dont know if it is a rasp pi thing or an i2c thing 
  #   or what hopefully I'll find out and let yinz know. 
  # LCD_ADDR = 0x3E        #alternatively
  # RGB_ADDR = 0x62   

  input_state   = 0x07 # increment cursor with each letter
  display_state = 0x0E # display on cursor on blink off
  shift_state   = 0x10 # don't shift text

  def __init___():
    time.sleep(0.05)      # wait after power on
    lcd_write_cmd(0x3C)   # 2 lines (bit 3) display on (bit 2)
    time.sleep(0.001)     # 
    lcd_write_cmd(0x0E)   # cursor on (bit 1) blink off (bit 0)
    time.sleep(0.001)     # 
    lcd_write_cmd(0x01)   # clear display
    time.sleep(0.001)     # 
    lcd_write_cmd(0x06)   # increment (bit 1) entire shift (bit 0)
    time.sleep(0.002)     # 

  #TODO figure out what heppens and what to do if string doesnt start at home
  #     and overruns the end
  def write_string(str):
     num = len(str)
     if(num > 32):
        num = 32
     i = 0
     row = 0
     while( (i < num) and (row < 2) ):
        if(str[i] == "\n") :
           set_cursor(1, 0)
           row += 1    
        else:
           if( (i == 16) and (row == 0) ):
              set_cursor(1, 0)
              row += 1
           lcd_write_data(ord(str[i]))
        i += 1

  def set_rgb(r, g, b):
     lcd_write_reg(0x00, 0x00)
     lcd_write_reg(0x01, 0x00)
     lcd_write_reg(0x08, 0xaa)   # set up whatever
     lcd_write_reg(0x04, r)      # red
     lcd_write_reg(0x03, g)      # green
     lcd_write_reg(0x02, b)      # ocre (jk blue)

  def clear():
     lcd_write_cmd(0x01)
     time.sleep(0.002)
     return_home()

  def return_home():
     lcd_write_cmd(0x02)
     time.sleep(0.002)

  def set_cursor(row, col):
     if(row == 0):
        lcd_write_cmd(col | 0x80)
     else:
        lcd_write_cmd(col | 0xc0)

  #### functions for setting various states for the display ####
  # note all inputs should be bools

  def set_display(on):
    if on:
      display_state |= 0x04
    else:
      display_state &= (~0x04)
    lcd_write_cmd(display_state)

  def set_cursor(on):
    if on:
      display_state |= 0x02
    else:
      display_state &= (~0x02)
    lcd_write_cmd(display_state)

  def set_blink(on):
    if on:
      display_state |= 0x01
    else:
      display_state &= (~0x01)
    lcd_write_cmd(display_state)

  def set_shift_cursor(on, inc):
    if on:
      input_state |= 0x01
    else:
      input_state &= (~0x01)
    if inc:
      input_state |= 0x02
    else:
      input_state &= (~0x02)
    lcd_write_cmd(input_state)

  # note: shifting display stops text shifting
  def set_shift_display(on, right):
    if on:
      shift_state |= 0x08
    else:
      shift_state &= (~0x08)
    if right:
      shift_state |= 0x04
    else:
      shift_state &= (~0x04)
    lcd_write_cmd(shift_state)

  #### low(ish) level functions ####

  def lcd_write_cmd(cmd):
     bus.write_byte_data(LCD_ADDR, 0x80, cmd)

  def lcd_write_data(data):
     # bus.write_byte(LCD_ADDR, 0x40)
     # bus.write_byte(LCD_ADDR, data)
     bus.write_byte_data(LCD_ADDR, 0x40, data)

  def lcd_write_reg(reg, data):
     bus.write_byte_data(RGB_ADDR, reg, data)
