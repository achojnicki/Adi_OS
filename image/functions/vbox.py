from .functions import system

import os

def remove_vbox_disk_file(vbox_disk_file):
    msg="Remove virtual box disk file"
    print(msg)

    os.remove(vbox_disk_file)

def remove_vbox_machine(vbox_machine_name):
	msg="""Removing vbox machine"""
	print(msg)

	cmd='vboxmanage unregistervm "{vbox_machine_name}" --delete'.format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)
    
def attach_loop_device_to_vbox_disk_file(loop_device, vbox_disk_file):
	msg="Attaching loop device to vbox disk file"
	print(msg)

	cmd='VBoxManage internalcommands createrawvmdk -filename {vbox_disk_file} -rawdisk {loop_device}'.format(
    	vbox_disk_file=vbox_disk_file,
        loop_device=loop_device)
	system(cmd)

def create_vbox_virtual_machine(vbox_machine_name, vbox_machine_dir,vbox_disk_file):
	msg="""creating virtualbox machine"""
	print(msg)

	cmd="""VBoxManage createvm --name "{vbox_machine_name}" --ostype "Linux_64" --register --basefolder {vbox_machine_dir} """.format(
		vbox_machine_name=vbox_machine_name,
		vbox_machine_dir=vbox_machine_dir)
	system(cmd)
	
	cmd=""" VBoxManage modifyvm "{vbox_machine_name}" --memory 1024 """.format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)
	
	cmd="""VBoxManage storagectl "{vbox_machine_name}" --name "SATA Controller" --add sata --controller IntelAhci""".format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)

	cmd="""VBoxManage storageattach "{vbox_machine_name}" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium {vbox_disk_file}""".format(
		vbox_machine_name=vbox_machine_name,
		vbox_disk_file=vbox_disk_file)
	system(cmd)

	cmd="""VBoxManage modifyvm "{vbox_machine_name}" --boot1 disk""".format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)
	
def stop_vbox_machine(vbox_machine_name):
	cmd="""VBoxManage controlvm "{vbox_machine_name}" poweroff""".format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)

def start_vbox_machine(vbox_machine_name):
	cmd='VBoxManage startvm "{vbox_machine_name}"'.format(
		vbox_machine_name=vbox_machine_name)
	system(cmd)

def convert_vbox_image(loop_device,vbox_generated_disk_file):
	try:
		os.remove(vbox_generated_disk_file)
	except:
		pass
		
	cmd='VBoxManage convertfromraw {loop_device} "{vbox_generated_disk_file}" --format VDI'.format(
		vbox_generated_disk_file=vbox_generated_disk_file,
		loop_device=loop_device)

	system(cmd)