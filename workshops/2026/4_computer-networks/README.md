# Réseaux informatiques pour systèmes robotiques

**Durée : 2 heures**
**Public : Étudiants ingénieurs en robotique – dernière année**
**Environnement : Ubuntu 24.04 / Python 3 / ROS 2**

## Objectifs pédagogiques

À l'issue de ce TP, vous serez capables de :

- Comprendre les composants d'une architecture réseau.
- Distinguer les protocoles TCP et UDP et leurs cas d'utilisation.
- Développer une communication client-serveur simple en Python.
- Utiliser les commandes Linux pour diagnostiquer un réseau.
- Découvrir les outils Nmap et Wireshark.
- Comprendre comment ROS 2 utilise le réseau pour communiquer entre plusieurs machines.
- Comprendre le rôle du DNS, du DHCP, des ports et du filtrage réseau.

---

# Fiches de TP

Le TP est organisé en plusieurs fiches thématiques contenant les explications nécessaires, les manipulations à réaliser et les exercices associés.

Les exercices doivent être réalisés dans l'ordre proposé afin de progresser des fondamentaux des réseaux jusqu'à leur utilisation dans un système robotique distribué.

| Fiche | Thématique | Lien |
|---|---|---|
| 01 | Architecture réseau | [Accéder à la fiche](01-network_architecture.md) |
| 02 | Configuration réseau | [Accéder à la fiche](02-tcp_udp_protocols.md) |
| 03 | TCP et UDP | [Accéder à la fiche](03-basic_commands_and_nmap.md) |
| 04 | Commandes réseau et Nmap | [Accéder à la fiche](04-network_analysis_with_wireshark.md) |
| 05 | Wireshark | [Accéder à la fiche](05-network_and_ros2.md) |
| 06 | ROS 2 et réseau | [Accéder à la fiche](06-dns_dhcp_ports_filtering.md) |
| 07 | Ports et filtrage | [Accéder à la fiche](07-synthesis_exercise.md) |

Les illustrations utilisées dans les fiches sont regroupées dans le dossier `img/`. Les scripts Python et leurs corrections sont disponibles dans le dossier `scripts/`.

---

# Ressources complémentaires

- [Documentation ROS 2](https://docs.ros.org/en/jazzy/)
- [Documentation Wireshark](https://www.wireshark.org/docs/)
- [Documentation Nmap](https://nmap.org/book/man.html)
- [Documentation Python — socket](https://docs.python.org/3/library/socket.html)
- [Documentation Ubuntu — Firewall](https://documentation.ubuntu.com/server/how-to/security/firewalls/)
