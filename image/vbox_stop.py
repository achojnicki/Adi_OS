#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
check_dirs(ROOT_DIR)
update_path()

stop_vbox_machine(VBOX_MACHINE_NAME)

#loop_device=get_loop_device(IMAGE_FILENAME)
#deatach_image(loop_device)