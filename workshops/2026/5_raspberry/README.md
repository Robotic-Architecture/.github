# Raspberry Pi setup

This is an attempt to make a simple walkthrough to a functional Raspberry for any robotic project

## Requirements
- Raspberry Pi 4
- Micro SD card
- Micro SD card reader
- Compatible power supply

## Image download

The Raspberry Pi 4 has an aarch64 architecture, Ubuntu realeases preinstalled image for raspberry. You can download the image from [here](https://cdimage.ubuntu.com/ubuntu/releases/24.04/release/ubuntu-24.04.4-preinstalled-server-arm64+raspi.img.xz).

## Image flash

The SD card is the only disk of the Raspberry, there is no internal storage. 
- Using a micro SD card reader, plug the micro SD card in your computer.
- Right-click on the .img.xz file and open with the built-in Disk Image Writer.
- Select the storage corresponding to the micro SD card and confirm.

## First boot setup

- Keep the micro SD card plugged in your computer, and open `system-boot`.
- Edit the file `network-config` :
    ```
    wifis:
    wlan0:
      optional: true
      access-points:
        "SSID":
          password: "MDP"
      dhcp4: true
      regulatory-domain: FR
    ```
    > [!NOTE]
    > Set SSID and MDP of an accessible network. Using your phone access point can be simpler for the next steps.

    > [!CAUTION]
    > Take care to only use spaces for indentation
- Edit the file `user-data` and set :
    ```
    ssh_pwauth: true
    ```
    > [!NOTE]
    > It allows you to connect to the raspberry using SSH

- Insert the micro SD card in the Raspberry and power it on.

## SSH connection

A useful tool to find your Raspberry Pi address on the network is [Angry IP Scanner](https://angryip.org/)