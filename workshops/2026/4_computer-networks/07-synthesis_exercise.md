# 7. Exercice de synthèse — Réseau d'une flotte robotique
> [!NOTE]
> **Durée : 15 minutes**

## Mise en situation

Vous disposez d'un système composé de :

- Deux robots autonomes équipés de ROS 2.
- Un ordinateur de supervision.
- Un switch Ethernet.
- Un routeur Wi-Fi.

Le robot 1 publie sa position sur un topic ROS 2. Le robot 2 doit récupérer ces informations et l'ordinateur de supervision doit pouvoir visualiser les données des deux robots.

Cependant, la communication ne fonctionne pas correctement.
> [!CAUTION]
> ## Questions
> - ⭐ 1. Dessiner l'architecture réseau du système.
> - ⭐ 2. Identifier les équipements nécessaires.
> - ⭐ 3. Expliquer comment vérifier la connectivité entre les machines.
> - ⭐ 4. Indiquer comment observer les communications avec Wireshark.
> - ⭐ 5. Donner deux causes possibles empêchant ROS 2 de communiquer entre les machines.
> - ⭐ 6. Expliquer le rôle que pourrait jouer un firewall dans ce problème.
