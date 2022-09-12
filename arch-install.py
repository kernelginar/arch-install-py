#!/usr/bin/env python3
import os

os.system("clear")

# edit /etc/pacman.conf
os.system("nano /etc/pacman.conf")

# update mirrors
os.system("pacman -Sy archlinux-keyring")

# disk configuration
os.system("clear")
os.system("lsblk")
print(" ")
disk_selection = input("Select disk (Example: /dev/vda, /dev/sda, /dev/nvme0n1): ")
os.system("cfdisk " f"{disk_selection}")

# format disk label
os.system("clear")
os.system("lsblk")
print(" ")

root_partition = input("Root partition (Example: /dev/vda1, /dev/sda1, /dev/nvme0n1p1): ")
os.system("mkfs.ext4 " f"{root_partition}")
os.system("mount " f"{root_partition} " "/mnt")
print(" ")

boot_partition = input("Boot partition (Example: /dev/vda1, /dev/sda1, /dev/nvme0n1p1): ")
os.system("mkdir -p /mnt/boot/efi")
os.system("mkfs.fat -F32 " f"{boot_partition}")
os.system("clear")

# install base packages
os.system("pacstrap /mnt base base-devel linux linux-headers linux-firmware git nano")

# create fstab file
os.system("genfstab -U /mnt > /mnt/etc/fstab")
os.system("mount " f"{boot_partition} " "/mnt/boot/efi")

os.system("cp $(pwd)/chroot.py /mnt")
os.system("arch-chroot /mnt /bin/bash")
os.system("rm -rf /mnt/chroot.py")
