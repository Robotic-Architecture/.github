# Basic Network Equipment: Hub, Switch and Router

This guide explains the differences between the main network devices: hubs, switches, routers and access points.

## 1. Hub

A **hub** connects multiple devices within the same local network.

When a device sends a message, the hub broadcasts it to **all connected devices**, regardless of the intended recipient.

- Operates at Layer 1 (Physical Layer) of the OSI model.
- Does not identify destination devices.
- Shares bandwidth between all connected devices.
- Mostly obsolete today.

## 2. Switch

A **switch** connects multiple devices within the same local network.

Unlike a hub, it learns the MAC addresses of connected devices and forwards Ethernet frames only to the appropriate destination port (when the destination is known).

- Operates primarily at Layer 2 (Data Link Layer).
- Uses MAC addresses to identify devices.
- Reduces unnecessary network traffic.
- Commonly used to connect computers, robots, sensors and servers.

## 3. Router

A **router** connects different IP networks and forwards packets between them.

For example, a router allows devices on a local network to communicate with the Internet.

- Operates at Layer 3 (Network Layer).
- Uses IP addresses to route packets.
- Connects different networks.
- Often provides DHCP and NAT services.

## 4. Access Point (AP)

An **access point** allows wireless devices to connect to a wired local network using Wi-Fi.

It acts as a bridge between wireless and wired devices.

- Primarily operates at Layer 2.
- Connects Wi-Fi clients to an Ethernet network.
- Does not necessarily provide routing or DHCP services.

## 5. Summary

| Device | Main function | OSI Layer |
|---|---|---|
| Hub | Broadcasts data to all ports | 1 |
| Switch | Connects devices within a LAN | 2 |
| Router | Connects different IP networks | 3 |
| Access Point | Connects Wi-Fi devices to a LAN | 2 |

## 6. Example: A robotic system

A typical robotic setup might look like this:

```text
                 INTERNET
                     |
                  ROUTER
                     |
                   SWITCH
                /    |     \
               /     |      \
          COMPUTER  ROBOT  SERVER
                     |
                ACCESS POINT
                     |
                 WIFI ROBOT
```

In a robotics environment:
- A **switch** connects multiple robots and computers through Ethernet.
- A **router** allows communication between different networks.
- An **access point** allows robots to communicate over Wi-Fi.
- A **hub** is generally avoided because it broadcasts all traffic to every connected device.