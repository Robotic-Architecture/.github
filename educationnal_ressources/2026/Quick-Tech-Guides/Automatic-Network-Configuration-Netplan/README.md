# Automatic Network Configuration with Netplan

This guide explains how to automatically connect an Ubuntu machine to multiple Wi-Fi networks and Ethernet interfaces using Netplan and systemd-networkd.

We use neither `NetworkManager` nor `iw`, assuming that the machine may not have an Internet connection and that all configuration must be performed using the tools already available on Ubuntu.

## 1. Configure Netplan

Create the configuration file:

```bash
sudo nano /etc/netplan/99-network.yaml
```

Add the following configuration, adapting the interface names, SSIDs and passwords:

```yaml
network:
  version: 2
  renderer: networkd

  wifis:
    wlan0:
      dhcp4: true
      optional: true
      access-points:
        "SSID_HOME":
          password: "PASSWORD_HOME"

        "SSID_SCHOOL":
          password: "PASSWORD_SCHOOL"

        "SSID_PHONE":
          password: "PASSWORD_PHONE"

  ethernets:
    eth0:
      dhcp4: true
      optional: true
```

- `renderer: networkd`: uses systemd-networkd to manage network interfaces.
- `dhcp4: true`: automatically obtains an IPv4 address using DHCP.
- `optional: true`: prevents an unavailable interface from blocking the system startup.
- `access-points`: lists the Wi-Fi networks the machine can connect to.

## 2. Apply the configuration

Generate and validate the configuration:

```bash
sudo netplan generate
```

This checks the configuration files and generates the corresponding systemd-networkd configuration.

Apply the configuration:

```bash
sudo netplan apply
```

This activates the new network configuration without requiring a reboot.

## 3. Verify the connection

Check network interfaces and their status:

```bash
networkctl status
```

Display assigned IP addresses:

```bash
ip addr
```

Display routing information:

```bash
ip route
```

Test Internet connectivity:

```bash
ping -c 4 8.8.8.8
```

Test DNS resolution:

```bash
ping -c 4 google.com
```

## 4. Troubleshooting

Check systemd-networkd logs:

```bash
journalctl -u systemd-networkd -b
```

Check the network startup service:

```bash
systemctl status systemd-networkd-wait-online.service
```

Restart network management:

```bash
sudo systemctl restart systemd-networkd
```

Protect configuration files containing Wi-Fi passwords:

```bash
sudo chmod 600 /etc/netplan/99-network.yaml
```