
# 2. Protocoles TCP et UDP

**Durée : 25 minutes**

## 2.1. Introduction

Lorsqu'une application souhaite communiquer avec une autre machine, elle doit utiliser un protocole de transport.

Les deux principaux protocoles de transport utilisés dans les réseaux IP sont TCP et UDP.

### TCP — Transmission Control Protocol

TCP est un protocole orienté connexion.

Avant de transmettre des données, les deux machines établissent une connexion.

TCP assure notamment :
- La livraison fiable des données, avec retransmission en cas de perte détectée.
- Le contrôle de l'ordre des données.
- La détection des erreurs.
- Le contrôle de flux et de congestion.

**Établissement d'une connexion TCP :**

![Établissement d'une connexion TCP](img/tcp_handshake.png)

L'établissement de la connexion utilise un mécanisme appelé *Three-Way Handshake* :

1. SYN : le client demande une connexion.
2. SYN-ACK : le serveur accepte la demande.
3. ACK : le client confirme la connexion.

### UDP — User Datagram Protocol

UDP est un protocole sans connexion.

Il transmet des datagrammes sans mettre en place de mécanisme natif de retransmission ou de confirmation de livraison.

Caractéristiques :
- Pas d'établissement préalable de connexion.
- Pas de garantie de livraison.
- Pas de garantie d'ordre.
- Faible surcharge protocolaire.

**Communication UDP :**

![Communication UDP](img/udp_communication.png)

## 2.2. Comparaison TCP / UDP

| Caractéristique | TCP | UDP |
|---|---|---|
| Connexion | Oui | Non |
| Livraison garantie | Oui, au niveau du transport | Non |
| Ordre des données | Garanti | Non garanti |
| Retransmission | Oui | Non, nativement |
| Contrôle de congestion | Oui | Non, nativement |
| Surcharge protocolaire | Plus importante | Plus faible |

### Exemples en robotique

| Application | Protocole envisageable |
|---|---|
| Transfert de fichiers de configuration | TCP |
| Communication avec un serveur de supervision | TCP |
| Transmission de télémétrie périodique | UDP |
| Transmission d'images | UDP ou TCP selon les besoins |
| Commandes de robot | TCP ou UDP selon les contraintes de l'application |

**Attention :** UDP ne garantit pas une faible latence. Il évite certains mécanismes de TCP, mais les performances dépendent aussi du réseau et de l'application.

## 2.3. Mise en pratique — Communication Python

Nous allons créer une communication entre deux programmes Python :

- Un programme serveur qui attend les messages.
- Un programme client qui transmet des commandes.

Les scripts de correction sont disponibles dans le dossier `scripts/`.

### Exercice 1 — Communication TCP

**Objectif :** créer une connexion TCP entre un client et un serveur.

1. Ouvrir deux terminaux.
2. Lancer le serveur :

```bash
python3 scripts/server_tcp.py
```

3. Dans le second terminal, lancer le client :

```bash
python3 scripts/client_tcp.py
```

4. Observer les messages échangés.
5. Identifier le moment où la connexion est établie.

### Exercice 2 — Communication UDP

**Objectif :** réaliser le même échange en utilisant UDP.

1. Lancer le serveur :

```bash
python3 scripts/server_udp.py
```

2. Dans un autre terminal, lancer le client :

```bash
python3 scripts/client_udp.py
```

3. Observer les messages échangés.

### Questions

- Quelle différence observez-vous entre les deux communications ?
- Quel est le rôle de la fonction `accept()` en TCP ?
- Pourquoi n'utilise-t-on pas `accept()` en UDP ?
- Quel port est utilisé par le serveur TCP ?
- Quel port est utilisé par le serveur UDP ?
- Est-il possible d'envoyer plusieurs messages UDP sans établir de connexion préalable ?
