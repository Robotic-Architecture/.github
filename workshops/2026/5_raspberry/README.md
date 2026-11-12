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
    > [!CAUTION]
    > Do not choose your computer storage if you do not want to erase your data.

  <img src="disk-image-writer.png" width="600">

## First boot setup

> [!NOTE]
>Cloud-init offers tools to configure the computer at the first boot. Two files can be edited in the `system-boot` partition :
>- `network-config` : configure netplan by editing `/etc/netplan/50-cloud-init.yaml`
>- `user-data` : configure system (ssh, user, settings, etc)

> [!CAUTION]
>Cloud-init reads these files once at the first boot and configure the Raspberry, **after the first boot they are ignored**. If errors happen after the first boot and you need to make changes you can :
>- Edit `/etc/netplan/50-cloud-init.yaml` instead of `network-config`
>- Edit `/etc/ssh/sshd_config.d/50-cloud-init.conf` instead of `user-data` for SSH

- Keep the micro SD card plugged in your computer, and open `system-boot`.
- Edit the file `network-config` with your SSID and password:
  ```
  network:
    version: 2

    ethernets:
      eth0:
        dhcp4: true
        optional: true

    wifis:
      wlan0:
        optional: true
        access-points:
          "SSID":
            password: "MDP"
        dhcp4: true
      regulatory-domain: FR
  ```

  > [!CAUTION]
  > Only use spaces for indentation

- Edit the file `user-data` :
  - Enable SSH :
    ```
    ssh_pwauth: true
    ```
  - Change username and password :
    ```
    chpasswd:
      expire: true
      users:
      - name: USERNAME
        password: PASSWORD
        type: text
    ```
  - Change hostname :
    ```
    hostname: HOSTNAME
    ```
    > [!NOTE]
    > The hostname is the name used to identify your Raspberry on the local network. You can use it instead of its IP address when connecting through SSH `ssh USERNAME@HOSTNAME`.
- Insert the micro SD card in the Raspberry and power it on.

## SSH connection

- Connect your computer to the same network you set for the Raspberry.
- Try and connect to your Raspberry with `ssh USERNAME@HOSTNAME`.
- Some configuration network only allows connection with an IP address. If previous command does not workd, find your Raspberry Pi address on the network. A useful tool I recommend is [Angry IP Scanner](https://angryip.org/).
  - Start the software
  - If your IP address is 192.168.10.50 you want to scan from 192.168.10.0 to 192.168.10.255
  - In the setting select Ping, MAC Vendor and MAC Address
  - Start the scan
  - Find your Raspberry, usually their MAC Address start with `DC:A6:32` or `E4:5F:01` or `D8:3A:DD` or `88:A2:9E`
  <img src="angry-ip.png" width="600">
- Connect via SSH to your Raspberry `ssh USERNAME@IP`

## Validation
> [!IMPORTANT]
> ⭐ Take a screenshot of your computer screen showing the ssh connection to the raspberry and its output
