#!/bin/sh

#io rw
mount -o remount,rw /dev/sda /

#tty
getty -L 19200 tty1 vt102&
getty -L 19200 tty2 vt102&
getty -L 19200 tty3 vt102&
getty -L 19200 tty4 vt102&
getty -L 19200 tty5 vt102&

#net
ifconfig lo 127.0.0.1
ifconfig lo netmask 255.0.0.0