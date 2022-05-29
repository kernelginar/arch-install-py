#!/usr/bin/python

import os
import sys
import time

os.system("clear")
print ("Kurulum 3 saniye icinde basliyor!")
time.sleep(3)
os.system("clear")

os.system("lsblk")
print (" ")
disk_selection = input("Diskinizi secin, /dev/???: ")
os.system("cfdisk " f"{disk_selection}")

os.system("clear")
os.system("lsblk")
root_partition = input("Root bolumunu secin, /dev/???: ")
os.system("mkfs.ext4 " f"{root_partition}")
os.system("mount " f"{root_partition} " "/mnt")

boot_partition = input("Boot bolumunu secin, /dev/???: ")
os.system("mkfs.fat -F32 " f"{boot_partition}")
os.system("mkdir -p /mnt/boot/efi")
os.system("mount " f"{boot_partition} " "/mnt/boot/efi")

swap_partition = input("Swap bolumu olusturduysaniz secin, /dev/???: ")
os.system("mkswap " f"{swap_partition}")
os.system("swapon " f"{swap_partition}")

os.system("clear")
print ('''Disk islemleri bitti. Simdi gerekli paketler kurulacak.
Kurulacak olan paketler: base base-devel linux-zen linux-zen-headers linux-firmware nano git
''')
os.system("pacstrap /mnt base base-devel linux-zen linux-zen-headers linux-firmware nano git")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
