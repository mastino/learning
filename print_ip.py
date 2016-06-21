#!/usr/bin/python
#
# printing ip address so
# designed for the Grove-LCD JHD1313M1
#
# Brian Gravelle
# June 2016
# There is no liscense and no warranty on this feel free to use it as you wish
#    but be warned I have no idea what I'm doing so you should look elsewhere.
#    If by some miracle you find this useful, I accept thanks in the form of 
#    chocolate and introductions to potential employers.

from lcd import *
import subprocess
from subprocess import Popen, PIPE

lcd_init()

ip = "0.0.0.0"

while( (ip is "0.0.0.0") or ((ip[0] is '1') and (ip[1] is '6') and (ip[2] is '9')) ):
   eth0 = subprocess.Popen(['/sbin/ifconfig', 'eth0'], stdout=PIPE)
   out, err = eth0.communicate()
   for line in out.split('\n'):
       line = line.lstrip()
       if line.startswith('inet addr:'):
           ip = line.split()[1][5:]

lcd_write_string(ip)
lcd_set_rgb(10,20,10)

      