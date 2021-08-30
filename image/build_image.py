#!/usr/bin/python3
from constants import *
from functions import *


check_permissions()
check_dirs(ROOT_DIR)

update_path()

prepare_image_file(IMAGE_FILENAME,IMAGE_FILE_SIZE)
prepare_mount_dir(BUILD_DIR)

attach_image(IMAGE_FILENAME)
loop_device=get_loop_device(IMAGE_FILENAME)


format(loop_device)
mount(loop_device,BUILD_DIR)

#copy root fs
copy_files(ROOT_DIR,BUILD_DIR)

#new kernel - no boot
#copy_file('../linux/arch/x86/boot/bzImage',VMLINUZ_LOCATION)
#copy_file('/boot/initrd.img-4.19.204',INITRD_LOCATION)


copy_file('/boot/vmlinuz-4.19.0-16-cloud-amd64',VMLINUZ_LOCATION)
copy_file('/boot/initrd.img-4.19.0-16-cloud-amd64',INITRD_LOCATION)

#copy kernel modules
#copy_files(MODULES_DIR,BUILD_DIR+'/lib/modules/4.19.204')

install_boot_image(BOOT_DIR,loop_device,WORKING_DIR)


umount(loop_device)
deatach_image(loop_device)
