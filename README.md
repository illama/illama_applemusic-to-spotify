# Apple Music vers Spotify - Convertisseur de playlists

---

## 🇫🇷 Présentation

Ce script Python permet de convertir facilement vos playlists ou votre bibliothèque Apple Music (exportée en XML) vers une playlist Spotify. Il est conçu pour être simple d'utilisation, rapide et fiable, sans interface graphique complexe.

- **Auteur** : illama
- **Licence** : MIT

---

## 🎯 Téléchargement rapide

### 📦 Version exécutable (Windows)
Pour une utilisation immédiate sans installation de Python :

1. **Téléchargez la dernière release** : [Releases GitHub](https://github.com/votre-username/illama_applemusic-to-spotify/releases)
2. **Extrayez le zip** et renommez `config.env` en `.env`
3. **Configurez vos identifiants Spotify** dans le fichier `.env`
4. **Lancez `AppleMusic-to-Spotify.exe`**

> 💡 **Recommandé pour les utilisateurs finaux** - Aucune installation de Python requise !

### 🐍 Version Python (Développeurs)
Pour les développeurs ou utilisateurs avancés :

```bash
git clone https://github.com/votre-username/illama_applemusic-to-spotify.git
cd illama_applemusic-to-spotify
pip install -r requirements.txt
python index.py
```

---

## 🌟 Fonctionnalités

- Conversion automatique de playlists Apple Music (URL) ou de bibliothèques exportées (XML)
- Création de playlists Spotify sur le compte de votre choix
- Support du changement de compte Spotify à tout moment
- Interface en ligne de commande, multilingue (français/anglais)
- Détection automatique du fichier `Library.xml` dans le dossier du script
- Gestion des erreurs et instructions claires pour l'utilisateur

---

## 🛠️ Installation

### Option 1: Version exécutable (Recommandée)
1. **Téléchargez** la dernière release depuis GitHub
2. **Extrayez** le contenu du zip
3. **Renommez** `config.env` en `.env`
4. **Configurez** vos identifiants Spotify dans `.env`

### Option 2: Version Python
1. **Cloner ou télécharger** ce dépôt
2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
3. **Créer un fichier `.env`** avec vos identifiants Spotify :
   ```env
   CLIENT_ID=VOTRE_CLIENT_ID
   CLIENT_SECRET=VOTRE_CLIENT_SECRET
   ```
4. **Créer une application sur le [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)** et ajouter l'URL de redirection :
   ```
   http://127.0.0.1:8888/callback
   ```

---

## 🚀 Utilisation

### Version exécutable
1. **Double-cliquez** sur `AppleMusic-to-Spotify.exe`
2. **Suivez les instructions** à l'écran

### Version Python
1. **Lancez le script** :
   ```bash
   python index.py
   ```
2. **Choisissez la langue** (français ou anglais)
3. **Sélectionnez la source** :
   - 1 : URL de playlist Apple Music
   - 2 : Fichier XML exporté d'Apple Music (placez `Library.xml` dans le dossier du script)
   - 3 : Fichier texte avec une chanson par ligne
4. **Suivez les instructions à l'écran**
5. **Connectez-vous à Spotify** (possibilité de changer de compte à chaque export)
6. **Récupérez le lien de votre nouvelle playlist Spotify !**

---

## 📂 Exemples de fichiers supportés

- **Apple Music** :
  - URL de playlist publique
  - Export XML de la bibliothèque (`Library.xml`)
- **Fichier texte** :
  - Une chanson par ligne, format libre

---

## 🔧 Configuration Spotify

### Créer une application Spotify
1. Allez sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Cliquez sur "Create App"
3. Remplissez les informations :
   - **App name** : Apple Music to Spotify Converter
   - **App description** : Convertisseur de playlists
   - **Website** : `http://localhost`
   - **Redirect URI** : `http://127.0.0.1:8888/callback`
4. Cliquez sur "Save"

### Configurer le fichier .env
```env
CLIENT_ID=votre_client_id_ici
CLIENT_SECRET=votre_client_secret_ici
```

---

## 🛠️ Développement

### Créer une release
```bash
# Installer PyInstaller
pip install pyinstaller

# Construire le .exe
python build_exe.py

# Créer un tag pour déclencher le workflow GitHub Actions
git tag v1.0.0
git push origin v1.0.0
```

### Structure du projet
```
illama_applemusic-to-spotify/
├── index.py              # Script principal
├── build_exe.py          # Script de build
├── requirements.txt      # Dépendances Python
├── .github/workflows/    # GitHub Actions
├── release/             # Package de release
└── docs/                # Documentation
```

---

## 🤝 Support & Communauté

- **Issues** : [GitHub Issues](https://github.com/votre-username/illama_applemusic-to-spotify/issues)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/illama_applemusic-to-spotify/discussions)
- **Discord** : Contactez **illama** sur Discord
- **Documentation** : Consultez [SETUP.md](SETUP.md) et [BUILD.md](BUILD.md)

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

> Script développé par **illama**.
