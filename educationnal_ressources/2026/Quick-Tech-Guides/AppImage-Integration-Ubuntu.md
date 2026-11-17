# Ajouter une AppImage au menu des applications Ubuntu

Ce guide explique comment rendre une application `.AppImage` accessible depuis la liste des applications GNOME, avec son logo.

## 1. Ranger l'AppImage

Créer un dossier pour les AppImages, puis déplacer le fichier dedans :

```bash
mkdir -p ~/Applications
mv ~/Téléchargements/monapp.AppImage ~/Applications/
chmod +x ~/Applications/monapp.AppImage
```

Remplacer `monapp.AppImage` par le nom réel du fichier.

## 2. Installer le logo

Si tu disposes d'un logo au format PNG (idéalement 256×256 ou 512×512) :

```bash
mkdir -p ~/.local/share/icons
cp logo.png ~/.local/share/icons/monapp.png
```

Le fichier `logo.png` doit être présent dans le dossier courant. Adapter son nom si nécessaire.

## 3. Créer le raccourci `.desktop`

Créer un fichier de raccourci dans le dossier des applications utilisateur :

```bash
nano ~/.local/share/applications/monapp.desktop
```

Y copier le contenu suivant :

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=Mon Application
Comment=Mon application AppImage
Exec=/home/TON_USER/Applications/monapp.AppImage
Icon=/home/TON_USER/.local/share/icons/monapp.png
Terminal=false
Categories=Utility;
```

Adapter les éléments suivants :

- `Name` : nom affiché dans le menu.
- `Exec` : chemin absolu vers l'AppImage.
- `Icon` : chemin absolu vers le logo.
- Remplacer `TON_USER` par ton nom d'utilisateur Linux (commande `whoami`).

## 4. Actualiser le menu

Exécuter :

```bash
update-desktop-database ~/.local/share/applications
```

Ubuntu devrait ensuite détecter automatiquement le raccourci. L'application peut être recherchée depuis le menu des applications GNOME.

## 5. (Optionnel) Extraire le logo de l'AppImage

Certaines AppImages embarquent déjà leur icône. Depuis le dossier contenant l'AppImage :

```bash
./monapp.AppImage --appimage-extract
```

Les fichiers extraits se trouvent dans `squashfs-root`. Chercher un fichier `.png` ou `.svg` correspondant au logo, puis le copier dans `~/.local/share/icons/`.

---

## Résumé

- AppImage : `~/Applications/monapp.AppImage`
- Logo : `~/.local/share/icons/monapp.png`
- Raccourci : `~/.local/share/applications/monapp.desktop`
