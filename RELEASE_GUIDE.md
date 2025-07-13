# Guide de Release GitHub - Apple Music to Spotify Converter

Ce guide vous explique comment créer et publier des releases GitHub avec le fichier .exe de votre convertisseur.

## 🎯 Vue d'ensemble

Votre projet est maintenant configuré pour créer automatiquement des releases GitHub avec :
- ✅ Fichier .exe autonome (13 MB)
- ✅ Documentation complète
- ✅ Fichier de configuration
- ✅ Workflow GitHub Actions automatisé

## 🚀 Méthodes de création de release

### Méthode 1: Automatique avec GitHub Actions (Recommandée)

1. **Créer un tag** :
   ```bash
   git add .
   git commit -m "Préparation release v1.0.0"
   git tag v1.0.0
   git push origin main
   git push origin v1.0.0
   ```

2. **Le workflow se déclenche automatiquement** :
   - Build du .exe sur Windows
   - Création de la release GitHub
   - Upload des fichiers

### Méthode 2: Manuel avec build local

1. **Construire le .exe** :
   ```bash
   python build_exe.py
   ```

2. **Créer la release sur GitHub** :
   - Allez sur votre repository GitHub
   - Cliquez sur "Releases" → "Create a new release"
   - Choisissez un tag (ex: v1.0.0)
   - Uploadez le contenu du dossier `release/`

## 📦 Contenu de la release

Chaque release contient :

```
📁 Release v1.0.0
├── 🎵 AppleMusic-to-Spotify.exe (13 MB)
├── 📖 README.md
├── ⚙️ SETUP.md  
├── 🔧 config.env
└── 📋 .env-example
```

## 🏷️ Convention de nommage des tags

Utilisez le format `vX.Y.Z` :
- **v1.0.0** - Première version stable
- **v1.1.0** - Nouvelles fonctionnalités
- **v1.1.1** - Corrections de bugs
- **v2.0.0** - Changements majeurs

## 📝 Description de release

Utilisez ce template pour vos releases :

```markdown
## 🎵 Apple Music to Spotify Converter v1.0.0

### 🆕 Nouveautés
- Conversion de playlists Apple Music vers Spotify
- Support des fichiers XML exportés d'Apple Music
- Import depuis des fichiers texte
- Interface bilingue (FR/EN)

### 📦 Installation
1. Téléchargez et extrayez le zip
2. Renommez `config.env` en `.env`
3. Configurez vos identifiants Spotify
4. Lancez `AppleMusic-to-Spotify.exe`

### ⚙️ Configuration requise
- Créez une app sur https://developer.spotify.com/dashboard
- Ajoutez `http://127.0.0.1:8888/callback` comme URL de redirection
- Copiez CLIENT_ID et CLIENT_SECRET dans `.env`

### 🔧 Fonctionnalités
- ✅ Conversion via URL de playlist
- ✅ Import XML automatique
- ✅ Import fichier texte
- ✅ Gestion multi-comptes Spotify
- ✅ Interface intuitive

### 🐛 Corrections
- Correction du parsing XML
- Amélioration de la recherche Spotify
- Meilleure gestion des erreurs

### 📋 Notes
- Taille du fichier : ~13 MB
- Compatible Windows 10/11
- Aucune installation requise
```

## 🔄 Workflow de développement

### Pour une nouvelle release :

1. **Développement** :
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   # Faites vos modifications
   git commit -m "Ajout nouvelle fonctionnalité"
   ```

2. **Test** :
   ```bash
   python build_exe.py
   # Testez le .exe généré
   ```

3. **Merge et release** :
   ```bash
   git checkout main
   git merge feature/nouvelle-fonctionnalite
   git tag v1.1.0
   git push origin main
   git push origin v1.1.0
   ```

## 🎯 Optimisations pour les releases

### Réduire la taille du .exe

Modifiez `build_exe.py` pour ajouter des optimisations :

```python
cmd = [
    'pyinstaller',
    '--onefile',
    '--strip',                    # Réduire la taille
    '--optimize=2',              # Optimisations Python
    '--exclude-module=matplotlib', # Exclure modules inutiles
    '--exclude-module=numpy',
    '--name=AppleMusic-to-Spotify',
    'index.py'
]
```

### Ajouter une icône

1. Créez un fichier `icon.ico`
2. Ajoutez `--icon=icon.ico` dans la commande PyInstaller

### Créer un installateur

Utilisez Inno Setup pour créer un installateur Windows :

```inno
[Setup]
AppName=Apple Music to Spotify Converter
AppVersion=1.0.0
DefaultDirName={pf}\AppleMusic-to-Spotify
DefaultGroupName=Apple Music to Spotify Converter

[Files]
Source: "release\AppleMusic-to-Spotify.exe"; DestDir: "{app}"
Source: "release\README.md"; DestDir: "{app}"
Source: "release\SETUP.md"; DestDir: "{app}"
Source: "release\config.env"; DestDir: "{app}"

[Icons]
Name: "{group}\Apple Music to Spotify Converter"; Filename: "{app}\AppleMusic-to-Spotify.exe"
Name: "{commondesktop}\Apple Music to Spotify Converter"; Filename: "{app}\AppleMusic-to-Spotify.exe"
```

## 📊 Statistiques de release

Gardez une trace de vos releases :

| Version | Date | Taille .exe | Téléchargements | Notes |
|---------|------|-------------|-----------------|-------|
| v1.0.0  | 2024-01-15 | 13 MB | 150 | Première release |
| v1.1.0  | 2024-02-01 | 12 MB | 300 | Optimisations |
| v1.2.0  | 2024-03-01 | 11 MB | 500 | Nouvelles fonctionnalités |

## 🔧 Dépannage des releases

### Le workflow GitHub Actions échoue

1. Vérifiez les logs dans l'onglet "Actions"
2. Assurez-vous que `requirements.txt` est à jour
3. Vérifiez que le code fonctionne localement

### Le .exe ne fonctionne pas

1. Testez sur une machine propre
2. Vérifiez les dépendances système
3. Ajoutez des logs de debug

### Problèmes de permissions

1. Vérifiez les permissions du repository
2. Assurez-vous que GitHub Actions est activé
3. Vérifiez les secrets si nécessaire

## 📞 Support

Pour les utilisateurs :
- Créez un fichier `CHANGELOG.md` pour l'historique
- Répondez aux issues GitHub rapidement
- Maintenez une documentation à jour

Pour les développeurs :
- Testez toujours avant de tagger
- Utilisez des messages de commit clairs
- Gardez une trace des changements

## 🎉 Prochaines étapes

1. **Première release** : Taggez `v1.0.0` et poussez
2. **Documentation** : Mettez à jour le README principal
3. **Promotion** : Partagez sur les réseaux sociaux
4. **Feedback** : Collectez les retours utilisateurs
5. **Améliorations** : Planifiez les prochaines versions

---

**Note** : Ce guide est spécifique à votre projet. Adaptez-le selon vos besoins et votre workflow de développement. 