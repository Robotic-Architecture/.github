# Connexion SSH par nom d'hôte

Ce guide permet de se connecter à un système Linux par son nom plutôt que par son adresse IP, même si celle-ci change. Dans cet exemple le nom de l'hôte choisi est pollux et le nom de l'utilisateur sur la raspberry est pi.

## 1. Sur le système distant

Définir un nom d'hôte unique :

```bash
sudo hostnamectl set-hostname pollux
```

Sur Debian ou Ubuntu, installer et activer SSH et mDNS :

```bash
sudo apt update
sudo apt install openssh-server avahi-daemon
sudo systemctl enable --now ssh avahi-daemon
```

Vérifier le nom et l'utilisateur :

```bash
hostname
whoami
```


## 2. Depuis l'ordinateur client

Les deux machines doivent être joignables sur le même réseau local.

```bash
ssh pi@pollux.local
```

Remplacer `pi` par le nom d'un utilisateur existant sur le système distant.

> [!CAUTION]
> ** dans le cas où ça n'a pas fonctionné **
> Sur le robot, vérifie la configuration d'Avahi :
> ```bash
> grep -E '^(host-name|domain-name)=' /etc/avahi/avahi-daemon.conf
> ```
> 
> Puis édite le fichier :
> ```bash
> sudo nano /etc/avahi/avahi-daemon.conf
> ```
> 
> Dans la section [server], ajoute ou modifie :
> ```bash
> [server]
> host-name=pollux
> domain-name=local
> ```
> 
> Ne crée pas une deuxième section [server] si elle existe déjà.
> 
> Redémarre Avahi :
> ```bash
> sudo systemctl restart avahi-daemon
> systemctl status avahi-daemon
> ```
> 
> Le journal doit maintenant indiquer :
> ```bash
> Host name is pollux.local
> ```
>

## 3. Utiliser un nom court

Pour se connecter avec `ssh pi@pollux`, créer ou modifier le fichier `~/.ssh/config` sur le client :

```sshconfig
Host pollux
    HostName pollux.local
    User pi
```

Puis :

```bash
chmod 600 ~/.ssh/config
ssh pollux
```

La commande `ssh pi@pollux` fonctionne également.
