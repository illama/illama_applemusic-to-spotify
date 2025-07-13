# Guide de Build - Apple Music to Spotify Converter

Ce guide vous explique comment créer un fichier .exe pour le convertisseur Apple Music vers Spotify.

## 🛠️ Prérequis

1. **Python 3.8+** installé sur votre système
2. **Git** pour cloner le repository
3. **Connexion Internet** pour télécharger les dépendances

## 📦 Installation des dépendances

```bash
# Cloner le repository
git clone https://github.com/votre-username/illama_applemusic-to-spotify.git
cd illama_applemusic-to-spotify

# Installer les dépendances
pip install -r requirements.txt
```

## 🔨 Build manuel

### Option 1: Utiliser le script de build automatique

```bash
python build_exe.py
```

Ce script va :
- Nettoyer les builds précédents
- Créer le fichier .exe avec PyInstaller
- Créer un package de release dans le dossier `release/`

### Option 2: Build manuel avec PyInstaller

```bash
# Nettoyer les builds précédents
rmdir /s build dist 2>nul
del *.spec 2>nul

# Créer le .exe
pyinstaller --onefile --name=AppleMusic-to-Spotify index.py
```

### Option 3: Build avec options avancées

```bash
pyinstaller --onefile \
            --name=AppleMusic-to-Spotify \
            --add-data=config.env;. \
            --hidden-import=spotipy \
            --hidden-import=spotipy.oauth2 \
            --hidden-import=requests \
            --hidden-import=bs4 \
            --hidden-import=dotenv \
            index.py
```

## 📁 Structure après build

Après un build réussi, vous aurez :

```
illama_applemusic-to-spotify/
├── dist/
│   └── AppleMusic-to-Spotify.exe    # Votre fichier .exe
├── build/                           # Fichiers temporaires de build
├── release/                         # Package de release (si utilisé build_exe.py)
│   ├── AppleMusic-to-Spotify.exe
│   ├── README.md
│   ├── SETUP.md
│   └── config.env
└── *.spec                          # Fichier de spécification PyInstaller
```

## 🚀 Création d'une release GitHub

### Méthode automatique (recommandée)

1. **Pousser un tag** pour déclencher le workflow GitHub Actions :
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. Le workflow va automatiquement :
   - Construire le .exe sur Windows
   - Créer une release GitHub
   - Attacher les fichiers nécessaires

### Méthode manuelle

1. **Construire le .exe** :
   ```bash
   python build_exe.py
   ```

2. **Créer une release sur GitHub** :
   - Allez sur votre repository GitHub
   - Cliquez sur "Releases"
   - Cliquez sur "Create a new release"
   - Choisissez un tag (ex: v1.0.0)
   - Uploadez le contenu du dossier `release/`

## 🔧 Dépannage

### Erreur "PyInstaller not found"
```bash
pip install pyinstaller
```

### Erreur "Module not found"
Ajoutez les modules manquants avec `--hidden-import` :
```bash
pyinstaller --onefile --hidden-import=nom_du_module index.py
```

### Fichier .exe trop volumineux
Utilisez `--exclude-module` pour exclure des modules inutiles :
```bash
pyinstaller --onefile --exclude-module=matplotlib --exclude-module=numpy index.py
```

### Problèmes de permissions
Sur Windows, lancez PowerShell en tant qu'administrateur.

## 📋 Vérification du build

1. **Tester le .exe** :
   ```bash
   cd dist
   AppleMusic-to-Spotify.exe
   ```

2. **Vérifier la taille** : Le fichier .exe devrait faire entre 20-50 MB

3. **Tester sur une machine propre** : Copiez le .exe sur un autre PC pour vérifier qu'il fonctionne sans Python installé

## 🎯 Optimisations

### Réduire la taille du .exe
```bash
pyinstaller --onefile --strip --optimize=2 index.py
```

### Ajouter une icône
```bash
pyinstaller --onefile --icon=icon.ico index.py
```

### Créer un installer
Utilisez des outils comme Inno Setup ou NSIS pour créer un installateur Windows.

## 📞 Support

En cas de problème :
1. Vérifiez que toutes les dépendances sont installées
2. Consultez les logs d'erreur de PyInstaller
3. Ouvrez une issue sur GitHub avec les détails de l'erreur 