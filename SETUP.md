# Configuration Spotify - Résolution de l'erreur d'authentification

## Étape 1: Créer une application Spotify

1. Allez sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Connectez-vous avec votre compte Spotify
3. Cliquez sur "Create App"
4. Remplissez les informations :
   - **App name** : `Apple Music to Spotify Converter` (ou un nom de votre choix)
   - **App description** : `Convert Apple Music playlists to Spotify`
   - **Website** : `http://localhost:8888`
   - **Redirect URI** : `http://127.0.0.1:8888/callback`
   - **API/SDKs** : Cochez "Web API"
5. Cliquez sur "Save"

## Étape 2: Récupérer vos identifiants

1. Dans votre application créée, notez :
   - **Client ID** (visible directement)
   - **Client Secret** (cliquez sur "Show Client Secret" pour le voir)

## Étape 3: Configurer les variables d'environnement

1. Renommez `config.env` en `.env`
2. Remplacez les valeurs dans le fichier `.env` :
   ```
   CLIENT_ID=votre_vrai_client_id
   CLIENT_SECRET=votre_vrai_client_secret
   ```

## Étape 4: Installer les dépendances

```bash
pip install spotipy python-dotenv requests beautifulsoup4
```

## Étape 5: Utilisation du convertisseur

Le script supporte maintenant 3 sources de données :

### Option 1: URL de playlist Apple Music
- Collez l'URL d'une playlist Apple Music publique

### Option 2: Fichier XML exporté d'Apple Music
- Exportez votre bibliothèque depuis Apple Music/iTunes
- Le script analysera automatiquement le fichier XML

### Option 3: Fichier texte simple
- Créez un fichier texte avec une chanson par ligne
- Format: `Nom de la chanson - Artiste` ou `Nom de la chanson Artiste`

## Étape 6: Analyser votre fichier XML (optionnel)

Si vous avez des problèmes avec votre fichier XML, utilisez le script d'analyse :

```bash
python analyze_xml.py votre_fichier.xml
```

Cela vous montrera la structure de votre fichier XML pour aider au débogage.

## Étape 7: Tester l'authentification

1. Lancez le script : `python index.py`
2. Choisissez votre option (1, 2 ou 3)
3. Une fenêtre de navigateur s'ouvrira pour l'authentification
4. Connectez-vous avec votre compte Spotify
5. Autorisez l'application

## Problèmes courants et solutions

### Erreur "Une erreur s'est produite"
- Vérifiez que l'URL de redirection est exactement `http://127.0.0.1:8888/callback`
- Assurez-vous que votre application est en mode "Development"
- Vérifiez que vos CLIENT_ID et CLIENT_SECRET sont corrects

### Erreur de port déjà utilisé
- Fermez les autres applications qui utilisent le port 8888
- Ou changez le port dans le code (ligne 47)

### Erreur de scope
- Les scopes demandés sont corrects pour la création de playlists
- Assurez-vous d'accepter toutes les permissions demandées

### Problèmes avec le fichier XML
- Utilisez `python analyze_xml.py votre_fichier.xml` pour analyser la structure
- Assurez-vous que le fichier XML est bien exporté depuis Apple Music/iTunes
- Vérifiez que le fichier n'est pas corrompu

## Utilisation

1. Lancez le script : `python index.py`
2. Choisissez votre source de données (1, 2 ou 3)
3. Suivez les instructions pour votre option
4. Entrez un nom pour votre nouvelle playlist Spotify
5. Attendez la conversion !

## Support

Si vous rencontrez encore des problèmes :
1. Vérifiez que tous les identifiants sont corrects
2. Assurez-vous que votre compte Spotify est actif
3. Vérifiez votre connexion internet
4. Essayez de redémarrer le script
5. Utilisez le script d'analyse XML si nécessaire 