#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
check_dirs(ROOT_DIR)
update_path()

attach_image(IMAGE_FILENAME)
loop_device=get_loop_device(IMAGE_FILENAME)



attach_loop_device_to_vbox_disk_file(loop_device,
	VBOX_DISK_FILE)

convert_vbox_image(loop_device,
	VBOX_GENERATED_DISK_FILE)


deatach_image(loop_device)
