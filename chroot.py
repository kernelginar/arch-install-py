import os
import time

#locale
locale = input("Select locale [en/tr]: ")
if locale == 'en':
    os.system("echo 'en_US.UTF-8' >> /etc/locale.gen")
    os.system("locale-gen")
    os.system("clear")
    os.system("touch /etc/locale.conf")
    os.system("echo 'LANG=en_US.UTF-8' >> /etc/locale.conf")
    os.system("touch /etc/vconsole.conf")
    os.system("echo 'KEYMAP=trq' >> /etc/vconsole.conf")
    os.system("clear")
elif locale == 'tr':
    os.system("echo 'tr_TR.UTF-8' >> /etc/locale.gen")
    os.system("locale-gen")
    os.system("clear")
    os.system("touch /etc/locale.conf")
    os.system("echo 'LANG=tr_TR.UTF-8' >> /etc/locale.conf")
    os.system("touch /etc/vconsole.conf")
    os.system("echo 'KEYMAP=trq' >> /etc/vconsole.conf")
    os.system("clear")


#local machine
hostname = input("Hostname: ")
os.system("echo " f"{hostname} " ">> /etc/hostname")


os.system("clear")

#root user password
print("Root user password: ")
os.system("passwd")
os.system("clear")

#packages
os.system("pacman -Sy networkmanager")
os.system("systemctl enable NetworkManager")
os.system("pacman -S xf86-input-synaptics xf86-input-libinput")
os.system("pacman -S ntfs-3g")

#grub
os.system("pacman -S grub efibootmgr os-prober")
os.system("grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Linux")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
os.system("clear")

#Add user
username = input("Username: ")
os.system("useradd -m -g users -G wheel,storage,power,audio,video -s /bin/bash " f"{username}")
print("Normal user password: ")
os.system("passwd " f"{username}")
os.system("clear")
os.system("exit")
