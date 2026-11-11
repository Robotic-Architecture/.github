# 3. Commandes réseau et Nmap
> [!NOTE]
> **Durée : 15 minutes**

Ubuntu fournit plusieurs commandes permettant de connaître la configuration réseau d'une machine et de diagnostiquer des problèmes de communication.

## 3.1. Commandes essentielles

| Commande | Fonction |
|---|---|
| `hostname` | Afficher le nom de la machine |
| `hostname -I` | Afficher les adresses IP |
| `ip addr` | Afficher les interfaces réseau et leurs adresses |
| `ip route` | Afficher la table de routage |
| `ping IP` | Tester la connectivité avec une machine |
| `ip neigh` | Afficher les voisins réseau connus |
| `ss -tuln` | Afficher les ports en écoute |
| `ip link` | Afficher les interfaces réseau |

### Quelques exemples

Afficher les adresses IP :

```bash
hostname -I
```

Afficher les interfaces réseau :

```bash
ip addr
```

Identifier la passerelle utilisée pour accéder à Internet :

```bash
ip route
```

Tester la communication avec une autre machine :

```bash
ping 192.168.1.10
```

Afficher les ports en écoute :

```bash
ss -tuln
```

## 3.2. Nmap — Network Mapper

Nmap est un outil permettant d'explorer un réseau et d'identifier les machines et services accessibles.

Installation :

```bash
sudo apt install nmap
```

Quelques commandes :

Scanner une machine :

```bash
nmap 192.168.1.10
```

Scanner un réseau local :

```bash
nmap 192.168.1.0/24
```

Scanner une plage de ports :

```bash
nmap -p 1-1000 192.168.1.10
```

Identifier les services associés aux ports :

```bash
nmap -sV 192.168.1.10
```
> [!CAUTION]
> ## 3.3. Exercice
> - ⭐ 1. Afficher l'adresse IP de votre machine.
> - ⭐ 2. Identifier votre passerelle réseau.
> - ⭐ 3. Tester la communication avec cette passerelle à l'aide de `ping`.
> - ⭐ 4. Scanner votre propre machine avec Nmap.
> - ⭐ 5. Identifier les ports ouverts avec `ss -tuln`.

**Remarque :** ne scannez que les machines du réseau de TP ou celles pour lesquelles vous disposez d'une autorisation.
