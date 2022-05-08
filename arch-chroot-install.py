#!/bin/sh

import os
import sys
import time
import datetime

os.system("clear")

print ('''Bunu çalıştırdığına göre Chroot olmuşsun demektir.
Güzel. Şimdi devam ediyoruz.''')

time.sleep(3)

os.system("clear")

print ("Şimdi zaman dilimini ayarlayacağım. Europe/Istanbul olacak.")

time.sleep(2)

os.system("ln -sf /usr/share/zoneinfo/Europe/Istanbul /etc/localtime")

print ("Tamamdır. Ayarladım. Şimdi saati senkronize edeceğim.")

time.sleep(2)

os.system("hwclock --systohc")

print ("Bu da tamam. Şimdi localini ayarlayacağım. Bu kurulum Türkçe olduğundan localini Türkçe ayarlayacağım. İstersen kurulum bittiğinde kendin değiştirebilirsin.")

time.sleep(2)

os.system("echo tr_TR.UTF-8 >> /etc/locale.gen")
os.system("locale-gen")
os.system("echo LANG=tr_TR.UTF-8 >> /etc/locale.conf")

print ("Locali ayarladım.")

time.sleep(2)

os.system("clear")

print ("Bana şimdi bilgisayarına vereceğin adı söylemen gerek.")
print (" ")

hostname = input("Bilgisayarımın adı: ")
os.system("echo "f"{hostname}" ">> /etc/hostname")

os.system("echo 127.0.0.1 localhost >> /etc/hosts")
os.system("echo ::1 localhost >> /etc/hosts")
os.system("echo 127.0.1.1 " f"{hostname}" ".localdomain "f"{hostname}")

os.system("clear")

print ("Hostname ayarladım. Şimdi internet için NetworkManager kuracağım.")

time.sleep(2)

os.system("pacman -S networkmanager")
os.system("systemctl enable NetworkManager")

print ("NetworkManager indirdim ve systemd başlangıcına ekledim. Yani sistemin her açıldığında NetworkManager otomatik başlatılacak.")

time.sleep(4)

os.system("clear")

print("Şimdi sana NTFS dosya sisteminin desteğini getireceğim. Paketin adı ntfs-3g")

time.sleep(2)

os.system("pacman -S ntfs-3g")

print (" ")
print ("Bu da bitti. Şimdi bir root parolası belirle.")

time.sleep (2)

os.system("passwd")

print (" ")
print ('''Şifreni ayarladın. Şimdi TouchPad desteğini indireceğim. Eğer kullanmazsan kurulumdan sonra kaldırırsın.
İki paket kurulucak. Bunlar xf86-input-synaptics ve xf86-input-libinput''')

time.sleep(5)

os.system("pacman -S xf86-input-synaptics xf86-input-libinput")

os.system("clear")

print ('''Bu da tamamlandı. Şimdi multilib reposunu etkinleştirmen gerek.

[multilib]
Include = /etc/pacman.d/mirrorlist

Bunun başındaki # işaretini kaldıracaksın.

Daha sonra istersen üst taraflarda #Color ibaresi var. Onun başındaki # işaretini de kaldır. Daha güzel gözüküyor :D

pacman.conf içindeki işlemlerin bu kadar olacak. Yaklaşık 20 saniye bekleyecek burası. 20 saniye sonra işleme geçeceğiz. Dikkatli bak.''')

time.sleep(20)

os.system("nano /etc/pacman.conf")

os.system("clear")

print ('''Bunu da hallettiğine göre devam edelim. Sistemin açılması için os-prober, grub ve efibootmgr paketlerini kuracağım.''')
print (" ")

os.system("pacman -Sy os-prober grub efibootmgr")
os.system("grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id="Arch Linux"")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")

os.system("clear")

print ('''BU işlem de tamam. Sırada kullanıcı eklemek var. Kullanıcı adını belirle.''')

username = input("Kullanici adi: ")

os.system("useradd -m -g users -G wheel,storage,power,video -s /bin/bash "f"{username}")

print ('''Şimdi bu kullanıcıya bir parola belirle.''')

os.system("passwd "f"{username}")

os.system("clear")

print ('''Az kaldı. Şimdi sudoers dosyasını düzenleyeceğiz.

½wheel ALL=(ALL:ALL) ALL satırının başındaki # işareti kaldırıyorsun. Sonra en alt satıra gelip

Defaults rootpw

yazıyorsun. Yine aynı şekilde 20 saniye bekliyor olacağım.''')

time.sleep(20)

os.system("EDITOR=nano visudo")

os.system("clear")

print (''''İşlemler bu kadar. Diğer kalan masaüstü kurmak, ekran kartı sürücüleri sende. Eğer ben yüklersem bu senin sistemin için bloat kalmış olur. Kendin halletsen daha iyi. Şimdi sırasıyla:

exit
umount -R /mnt
reboot

komutlarını yaz. Eğer kurulumda bir aksilik çıkmadıysa seni GRUB ekranı karşılaması lazım. Güle güle kullan! :) ''')
