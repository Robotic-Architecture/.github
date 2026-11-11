# 5. Comment ROS 2 utilise le réseau ?

**Durée : 15 minutes**

## 5.1. Architecture de communication

ROS 2 permet de faire communiquer plusieurs nœuds, potentiellement exécutés sur des machines différentes.

Contrairement à une architecture client-serveur classique, ROS 2 s'appuie sur un middleware de communication distribué appelé DDS (*Data Distribution Service*).

![Architecture de communication ROS 2 et DDS](img/ros2_dds_architecture.png)

Le fonctionnement général est le suivant :

1. Chaque nœud ROS 2 est un processus indépendant.
2. Les nœuds échangent des informations via des topics, services et actions.
3. ROS 2 utilise une couche middleware basée sur DDS.
4. DDS permet notamment la découverte des participants et la communication entre les nœuds.
5. Les données transitent par le réseau IP.

Les implémentations DDS classiques utilisent généralement UDP/IP pour les échanges de données, mais le transport exact dépend de l'implémentation et de sa configuration.

## 5.2. Exemple : deux machines ROS 2

Imaginons deux machines connectées au même switch :

- **Machine A :** un robot publiant sa position sur `/robot/odom`.
- **Machine B :** un ordinateur de supervision qui récupère les informations du robot.

Les deux machines doivent pouvoir communiquer sur le réseau.

### Quelques commandes ROS 2

Afficher les nœuds actifs :

```bash
ros2 node list
```

Afficher les topics disponibles :

```bash
ros2 topic list
```

Observer les messages transmis :

```bash
ros2 topic echo /robot/odom
```

Afficher le domaine ROS 2 :

```bash
echo $ROS_DOMAIN_ID
```

Définir un domaine :

```bash
export ROS_DOMAIN_ID=10
```

## 5.3. Questions

1. Comment les machines découvrent-elles les nœuds ROS 2 présents sur le réseau ?
2. Est-il nécessaire de créer manuellement une connexion TCP entre chaque nœud ?
3. Que se passe-t-il si deux machines utilisent des `ROS_DOMAIN_ID` différents ?
4. Pourquoi un firewall peut-il empêcher la découverte des nœuds ROS 2 ?
5. Quel est l'intérêt de pouvoir exécuter les nœuds sur plusieurs machines ?

**À retenir :** ROS 2 ne repose pas simplement sur une communication client-serveur. DDS gère la découverte et les échanges distribués entre les participants.
