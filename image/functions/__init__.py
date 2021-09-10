#!/usr/bin/python
from .functions import system
from .vbox import *
from constants import *

import os 
import sys
import subprocess

import json
import shutil


def check_dirs(root_dir):
    if not root_dir.replace('./','') in os.listdir():
        msg='cd...'
        print(msg)

        sys.exit(0)

def check_permissions():
    msg="Checking permissions..."
    print(msg)

    if os.getuid()!=0:
        print('Have to run as root')
        sys.exit(0)

def update_path():
    msg="Updating $PATH"
    print(msg)

    os.environ['PATH']=os.environ['PATH']+':/sbin:/usr/sbin'

def prepare_mount_dir(image_mount_dir):
    msg="Preparing working dir..."
    print(msg)

    if not os.path.isdir(image_mount_dir):
        os.mkdir(image_mount_dir)
        
def prepare_image_file(image_filename,size=100):
    """size in MB"""
    msg="Preparing image file..."
    print(msg)

    count=size*1024
    cmd="dd if=/dev/zero of=./{image_filename} bs=1024 count={count}".format(
        image_filename=image_filename,
        count=count
        )
    
    system(cmd)

def attach_image(image_filename):
    msg="Attaching image file"
    print(msg)

    cmd="losetup -fP {image}".format(image=image_filename)
    system(cmd)

def deatach_image(loop_device):
    msg="Deataching image"
    print(msg)

    cmd="losetup -d {loop_device}".format(loop_device=loop_device)
    system(cmd)

def get_loop_device(image_filename):
    msg="Finding loop device with assosiation with image file"
    print(msg)

    cmd='losetup -J'
    process=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    output=process.communicate()[0]
    try:
        data=json.loads(output)['loopdevices']
        for a in data:
            if image_filename in a['back-file']:
                return a['name']
    except:
        pass
    raise Exception('cannot find loop device')

def format(loop_device,filesystem='ext4'):
    msg="Creating filesystem"
    print(msg)

    cmd="mkfs.{filesystem} {loop_device}".format(loop_device=loop_device,filesystem=filesystem)
    system(cmd)
    
def mount(loop_device,mount_point):
    msg="Mounting image file on loop device"
    print(msg)

    cmd="mount {loop_device} {mount_point}".format(loop_device=loop_device,mount_point=mount_point)
    system(cmd)

def umount(loop_device):
    msg="umounting image"
    print(msg)

    cmd="""umount {loop_device}""".format(loop_device=loop_device)
    system(cmd)

def install_boot_image(boot_dir,loop_device,working_dir):
    os.chdir(boot_dir)
    cmd="""../../tools/extlinux.x64 --instal ./ --device {loop_device}""".format(
        loop_device=loop_device,
        )
    system(cmd)
    os.chdir(working_dir)

def copy_file(src, dest):
    cmd="""cp "{src}" "{dest}" """.format(
        src=src,
        dest=dest)
    system(cmd)

def copy_files(src, dest):
    cmd="""cp -R "{src}/"* "{dest}" """.format(
        src=src,
        dest=dest)
    system(cmd)
    