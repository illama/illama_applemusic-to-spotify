# Apple Music vers Spotify - Convertisseur de playlists

---

## 🇫🇷 Présentation

Ce script Python permet de convertir facilement vos playlists ou votre bibliothèque Apple Music (exportée en XML) vers une playlist Spotify. Il est conçu pour être simple d'utilisation, rapide et fiable, sans interface graphique complexe.

- **Auteur** : illama
- **Licence** : MIT

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

## 🤝 Support & Communauté

- Pour toute question ou suggestion, contactez **illama** sur Discord.
- Rejoignez la communauté pour des mises à jour et du support.

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

> Script développé par **illama**.
