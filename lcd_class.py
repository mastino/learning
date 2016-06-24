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

  # in a real language I would make these constant
  default_display_state = 0x0E # display on, cursor on, blink off
  default_input_state   = 0x06 # increment cursor (don't move text)
  default_shift         = 0x10 # for one time shifts of text or cursor

  input_state   = default_input_state  
  display_state = default_display_state

  def __init__(self):
    time.sleep(0.05)           # wait after power on
    self.lcd_write_cmd(0x3C)   # 2 lines (bit 3) display on (bit 2)
    time.sleep(0.001)          # 
    self.lcd_write_cmd(0x0E)   # cursor on (bit 1) blink off (bit 0)
    time.sleep(0.001)          # 
    self.lcd_write_cmd(0x01)   # clear display
    time.sleep(0.001)          # 
    self.lcd_write_cmd(0x06)   # increment (bit 1) entire shift (bit 0)
    time.sleep(0.002)          # 
    self.set_default_states()

  #TODO figure out what heppens and what to do if string doesnt start at home
  #     and overruns the end
  def write_string(self, str):
     num = len(str)
     if(num > 32):
        num = 32
     i = 0
     row = 0
     while( (i < num) and (row < 2) ):
        if(str[i] == "\n") :
           self.move_cursor(1, 0)
           row += 1    
        else:
           if( (i == 16) and (row == 0) ):
              self.move_cursor(1, 0)
              row += 1
           self.lcd_write_data(ord(str[i]))
        i += 1

  def set_rgb(self, r, g, b):
     self.lcd_write_reg(0x00, 0x00)
     self.lcd_write_reg(0x01, 0x00)
     self.lcd_write_reg(0x08, 0xaa)   # set up whatever
     self.lcd_write_reg(0x04, r)      # red
     self.lcd_write_reg(0x03, g)      # green
     self.lcd_write_reg(0x02, b)      # ocre (jk blue)

  # note: sets text shift control to inc
  def clear(self):
     self.lcd_write_cmd(0x01)
     time.sleep(0.002)
     self.return_home() # this may be redundant

  def return_home(self):
     self.lcd_write_cmd(0x02)
     time.sleep(0.002)

  def move_cursor(self, row, col):
     if(row == 0):
        self.lcd_write_cmd(col | 0x80)
     else:
        self.lcd_write_cmd(col | 0xc0)

  #### functions for setting various states for the display ####
  # note all inputs should be bools

  def set_default_states(self):
    self.lcd_write_cmd(self.default_display_state)
    self.lcd_write_cmd(self.default_input_state)
    self.input_state   = self.default_input_state  
    self.display_state = self.default_display_state


  def set_display(self, on):
    if on:
      self.display_state |= 0x04
    else:
      self.display_state &= (~0x04)
    self.lcd_write_cmd(self.display_state)

  def set_cursor(self, on):
    if on:
      self.display_state |= 0x02
    else:
      self.display_state &= (~0x02)
    self.lcd_write_cmd(self.display_state)

  # makes the cursor blink
  def set_blink(self, on):
    if on:
      self.display_state |= 0x01
    else:
      self.display_state &= (~0x01)
    self.lcd_write_cmd(self.display_state)

  # note: text chooses shift text (true) or cursor
  #       inc does left or right; shifting text keeps the cursor in place
  #           and moves the text. moving text right doesn't work well
  def set_shift_text(self, text, inc):
    if text:
      self.input_state |= 0x01
    else:
      self.input_state &= (~0x01)
    if inc:
      self.input_state |= 0x02
    else:
      self.input_state &= (~0x02)
    self.lcd_write_cmd(self.input_state)

  # note: does a one time shift text (T) / cursor (F), Right (T) / left (F)
  def shift_text(self, text, right):
    shift = self.default_shift
    if text:
      shift |= 0x08
    else:
      shift &= (~0x08)
    if right:
      shift |= 0x04
    else:
      shift &= (~0x04)
    self.lcd_write_cmd(shift)

  #### low(ish) level functions ####

  def lcd_write_cmd(self, cmd):
     self.bus.write_byte_data(self.LCD_ADDR, 0x80, cmd)

  def lcd_write_data(self, data):
     # bus.write_byte(LCD_ADDR, 0x40)
     # bus.write_byte(LCD_ADDR, data)
     self.bus.write_byte_data(self.LCD_ADDR, 0x40, data)

  def lcd_write_reg(self, reg, data):
     self.bus.write_byte_data(self.RGB_ADDR, reg, data)
