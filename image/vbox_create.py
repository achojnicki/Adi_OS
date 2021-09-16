#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
update_path()

attach_image(IMAGE_FILENAME)
loop_device=get_loop_device(IMAGE_FILENAME)



attach_loop_device_to_vbox_disk_file(loop_device,
	VBOX_DISK_FILE)
create_vbox_virtual_machine(VBOX_MACHINE_NAME,
	VBOX_MACHINE_DIR,
	VBOX_DISK_FILE)
