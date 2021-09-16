#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
update_path()
try:
	remove_vbox_disk_file(VBOX_DISK_FILE)
except:
	pass
remove_vbox_machine(VBOX_MACHINE_NAME)
