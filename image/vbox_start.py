#!/usr/bin/python3

from functions import *
from constants import *


check_permissions()
check_dirs(ROOT_DIR)
update_path()

start_vbox_machine(VBOX_MACHINE_NAME)