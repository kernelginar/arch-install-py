#!/bin/sh

import os
import sys
import datetime
import time

os.system("clear")

print ("Arch Linux kurulum scriptine hoşgeldiniz. Kurulum Türkçe devam edecektir ve UEFI olacaktır. Eğer BIOS kurulum istiyorsanız BIOS kurulum scripti için bekleyiniz.")

time.sleep(4)

os.system("clear")

os.system("lsblk")

print ('''
Diskinizi görebiliyor musunuz?
[1] Evet
[2] Hayır
''')

ask_disk = input("Seçiniz: ")

if ask_disk == '1':
    os.system("clear")
    os.system("lsblk")
    print (" ")
    disk_selection = input("/dev/???: ")
    print (disk_selection)

    print ('''300M EFI System
RAM'inizin 2 katı Linuxswap (Opsiyonel
Kalan alan Linux filesystem
''')

    time.sleep(3)

    os.system("cfdisk "f"{disk_selection}")

    os.system("clear")
    os.system("mkdir -p /mnt/boot/efi")
    os.system("lsblk")
    print (" ")
    print ('''Şimdi diskleri bağlaman gerek. Bunun için sana yardımcı olacağım.
İlk önce /mnt yani root bölümünü bağlayalım. Üstüne Boot bölümünü. Ne dersin?
Korkma sana yardımcı olacağım. Bana root kısmı için ayırdığın diski söyle yeter.''')
    root_disk = input("/dev/???: ")
    os.system("mount "f"{root_disk} " "/mnt")
    print ('''Şimdi root bölümünü bağladık. Sıra boot bölümünde. Bana boot bölümünü söyle.''')
    boot_disk = input("/dev???: ")
    os.system("mount "f"{boot_disk} " "/mnt/boot/efi")
    print ('''Tamamdır! Boot bölümünü de bağladık. Şimdi eğer swap alanı oluşturduysan bana söyle. Hemen etkinleştireyim.
[1] Swap alanı oluşturdum.
[2] Swap alanı oluşturmadım.''')
    swap_ask = input("Seçiniz: ")
    if swap_ask == '1':
        os.system("clear")
        os.system("lsblk")
        swap_disk = input("/dev/???: ")
        os.system("mkswap "f"{swap_disk}")
        os.system("swapon "f"{swap_disk}")
        os.system("clear")
        os.system("lsblk")
        print ("İşlem tamamlandı.")
    elif swap_ask == '2':
        os.system("clear")
        print ("Şimdi biraz rahatla. Sistem dosyalarını kuracağım.")
        time.sleep(4)
        os.system("pactsrap /mnt base base-devel linux-zen linux-zen-headers linux-firmware git nano neovim vim")
        os.system("genfstab -U /mnt >> /mnt/etc/fstab")
