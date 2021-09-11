#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
check_dirs(ROOT_DIR)
update_path()

attach_image(IMAGE_FILENAME)
loop_device=get_loop_device(IMAGE_FILENAME)


convert_vbox_image(loop_device,
	VBOX_GENERATED_DISK_FILE)


deatach_image(loop_device)
