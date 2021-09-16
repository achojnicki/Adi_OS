#!/usr/bin/python3
from constants import *
from functions import *


check_permissions()

update_path()


attach_image(IMAGE_FILENAME)
loop_device=get_loop_device(IMAGE_FILENAME)

mount(loop_device,BUILD_DIR)
