import os

os.system("clear")
os.system("lsblk")
print(" ")
disk_selection = input("Select disk with /dev, /dev/???: ")
os.system("cfdisk " f"{disk_selection}")

os.system("clear")
os.system("lsblk")
print(" ")

root_partition = input("Root partition with /dev/???: ")
os.system("mkfs.ext4 " f"{root_partition}")
os.system("mount " f"{root_partition} " "/mnt")
print(" ")

boot_partition = input("Boot partition with /dev, /dev/???: ")
os.system("mkdir -p /mnt/boot/efi")
os.system("mkfs.fat -F32 " f"{boot_partition}")
os.system("mount " f"{boot_partition} " "/mnt/boot/efi")
os.system("clear")

os.system("pacstrap /mnt base base-devel linux-zen linux-zen-headers linux-firmware git nano")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("cp $(pwd)/chroot.py /mnt")
os.system("arch-chroot /mnt /bin/bash")
os.system("python unmount.py")
