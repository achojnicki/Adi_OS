#!/usr/bin/python3

from functions import *
from constants import *

loop_device=get_loop_device(IMAGE_FILENAME)

try:
	umount(loop_device)

except:
	pass
	
deatach_image(loop_device)