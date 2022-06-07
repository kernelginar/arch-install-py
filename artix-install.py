import os

os.system("clear")

os.system("lsblk")
print(" ")
disk_selection = input("/dev/???: ")
os.system("cfdisk " f"{disk_selection}")

os.system("clear")
os.system("lsblk")
root_partition = input("/dev/???: ")
os.system("mkfs.ext4 " f"{root_partition}")
os.system("mount " f"{root_partition} " "/mnt")
print(" ")

boot_partition = input("/dev/???: ")
os.system("mkfs.fat -F32 " f"{boot_partition}")
os.system("mkdir -p /mnt/boot/efi")
os.system("mount " f"{boot_partition} " "/mnt/boot/efi")

os.system("clear")
os.system("basestrap -i base base-devel linux linux-headers linux-firmware git nano artix-archlinux-support")
