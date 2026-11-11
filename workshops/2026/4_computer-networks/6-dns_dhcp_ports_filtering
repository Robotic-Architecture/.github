# 6. DNS, DHCP, ports et filtrage

**Durée : 10 minutes**

## 6.1. Les services réseau

### DHCP — Dynamic Host Configuration Protocol

Le DHCP permet d'attribuer automatiquement une configuration réseau à une machine.

Cette configuration peut contenir :
- Une adresse IP.
- Un masque de sous-réseau.
- Une passerelle.
- Un ou plusieurs serveurs DNS.

Exemple : lorsqu'un robot se connecte au Wi-Fi, le routeur peut lui attribuer automatiquement l'adresse `192.168.1.20`.

### DNS — Domain Name System

Le DNS permet d'associer un nom de domaine à une adresse IP.

Exemple :

```text
www.google.com → adresse IP du serveur
```

Cela évite de devoir mémoriser les adresses IP des machines et services.

### ARP — Address Resolution Protocol

ARP permet de retrouver l'adresse MAC correspondant à une adresse IPv4 sur le réseau local.

Exemple :

```text
192.168.1.20 → AA:BB:CC:DD:EE:FF
```

### Passerelle (Gateway)

La passerelle permet à une machine de communiquer avec des réseaux extérieurs à son réseau local.

Elle correspond généralement à l'adresse IP du routeur local.

## 6.2. Ports réseau

Une adresse IP permet d'identifier une interface réseau. Un port permet d'identifier un service ou une application sur cette machine.

Exemples :

| Port | Protocole | Service |
|---|---|---|
| 22 | TCP | SSH |
| 53 | UDP/TCP | DNS |
| 67 / 68 | UDP | DHCP |
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 5000 | TCP | Serveur Python du TP |

Un service doit écouter sur un port pour pouvoir recevoir des communications.

## 6.3. Firewall et filtrage

Un firewall (pare-feu) permet de contrôler les communications réseau entrantes et sortantes.

Il peut notamment autoriser ou bloquer :
- Une adresse IP.
- Un port.
- Un protocole.
- Une direction de communication.

### Exemple avec UFW

UFW (*Uncomplicated Firewall*) est un outil simplifié de gestion du firewall sous Ubuntu.

Afficher son état :

```bash
sudo ufw status
```

Autoriser le port SSH :

```bash
sudo ufw allow 22/tcp
```

Autoriser le serveur TCP Python :

```bash
sudo ufw allow 5000/tcp
```

Bloquer le port UDP 5001 :

```bash
sudo ufw deny 5001/udp
```

**Attention :** un port autorisé par le firewall ne garantit pas que le service soit accessible. Il faut également que le service soit actif, qu'il écoute sur la bonne interface et que le routage fonctionne.
