# Convertisseur Apple Music vers Spotify - Support XML et playlists

import requests
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import xml.etree.ElementTree as ET
import traceback
import json

# Load environment variables
load_dotenv()

# Système de langues
LANGUAGES = {
    'fr': {
        'title': '=== Convertisseur Apple Music vers Spotify ===',
        'option1': 'URL de playlist Apple Music',
        'option2': 'Fichier XML exporté d\'Apple Music (automatique)',
        'option3': 'Fichier texte avec liste de chansons',
        'choose_option': 'Choisissez votre option (1, 2 ou 3): ',
        'invalid_option': 'Option invalide',
        'searching_xml': 'Recherche automatique du fichier XML...',
        'xml_found': 'Fichier XML trouvé: {}',
        'xml_not_found': 'Aucun fichier XML trouvé dans le dossier courant.',
        'xml_files_searched': 'Fichiers recherchés: {}',
        'playlist_url_prompt': 'URL de la playlist Apple Music: ',
        'text_file_prompt': 'Chemin vers le fichier texte: ',
        'found_songs': 'Trouvé {} chansons à convertir',
        'no_songs': '❌ Aucune chanson trouvée',
        'playlist_name_prompt': 'Entrez le nom de la nouvelle playlist: ',
        'connected_as': 'Connecté en tant que: {}',
        'playlist_created': 'Playlist créée: {}',
        'searching': 'Recherche ({}/{}): {}',
        'added': ' ✓ Ajouté: {} - {}',
        'not_found': ' ✗ Aucun résultat pour: {}',
        'summary': '=== Résumé ===',
        'found_added': 'Chansons trouvées et ajoutées: {}/{}',
        'not_found_tracks': 'Chansons non trouvées ({}):',
        'playlist_complete': 'Playlist complète: {}',
        'conversion_complete': '✅ Conversion terminée! Playlist disponible: {}',
        'press_enter': 'Appuyez sur Entrée pour quitter...',
        'error_auth': 'Erreur d\'authentification Spotify: {}',
        'error_xml': 'Erreur lors de la lecture du fichier XML: {}',
        'error_playlist': 'Erreur lors de la création de la playlist: {}',
        'error_unexpected': 'Erreur inattendue: {}',
        'error_details': 'Détails de l\'erreur:',
        'auth_check': 'Vérifiez que:',
        'auth_check1': '1. Votre CLIENT_ID et CLIENT_SECRET sont corrects',
        'auth_check2': '2. L\'URL de redirection http://127.0.0.1:8888/callback est configurée dans votre app Spotify',
        'auth_check3': '3. Votre application Spotify est en mode \'Development\'',
        'env_error': 'Erreur: CLIENT_ID et CLIENT_SECRET doivent être définis dans le fichier .env',
        'env_help': 'Veuillez créer un fichier .env avec:',
        'env_client_id': 'CLIENT_ID=votre_client_id_spotify',
        'env_client_secret': 'CLIENT_SECRET=votre_client_secret_spotify',
        'cannot_continue': 'Impossible de continuer sans authentification Spotify',
        'xml_reading': 'Tentative de lecture du fichier XML: {}',
        'xml_loaded': 'Fichier XML chargé. Racine: {}',
        'method1': 'Méthode 1: Recherche des clés Name/Artist...',
        'name_keys_found': 'Clés \'Name\' trouvées: {}',
        'artist_keys_found': 'Clés \'Artist\' trouvées: {}',
        'found_song': 'Trouvé: {}',
        'method2': 'Méthode 2: Recherche de tous les textes...',
        'strings_found': 'Éléments \'string\' trouvés: {}',
        'text_found': 'Texte trouvé: {}',
        'method3': 'Méthode 3: Recherche dans les dictionnaires...',
        'dicts_found': 'Éléments \'dict\' trouvés: {}',
        'found_in_dict': 'Trouvé dans dict: {}',
        'total_songs': 'Total des chansons trouvées: {}',
        'too_many_songs': 'Trop de chansons trouvées ({}), limitation à 1000',
        'xml_parse_error': 'Erreur de parsing XML: {}',
        'xml_corrupted': 'Le fichier XML semble corrompu ou mal formaté',
        'file_not_exists': 'Erreur: Le fichier {} n\'existe pas',
        'not_xml_file': 'Attention: Le fichier {} ne semble pas être un fichier XML',
        'text_songs_found': 'Trouvé {} chansons dans le fichier texte',
        'text_error': 'Erreur lors de la lecture du fichier texte: {}',
        'playlist_error': 'Erreur lors de la récupération de la playlist: {}',
        'account_selection': '=== Sélection du compte Spotify ===',
        'current_account': 'Compte actuel: {}',
        'change_account': 'Changer de compte',
        'use_current': 'Utiliser le compte actuel',
        'account_choice': 'Voulez-vous changer de compte Spotify ? (y/n): ',
        'logging_out': 'Déconnexion du compte actuel...',
        'new_auth': 'Authentification avec un nouveau compte...',
        'account_changed': 'Compte changé avec succès !',
        'logout_success': 'Déconnexion réussie.',
        'logout_error': 'Erreur lors de la déconnexion: {}'
    },
    'en': {
        'title': '=== Apple Music to Spotify Converter ===',
        'option1': 'Apple Music playlist URL',
        'option2': 'Exported Apple Music XML file (automatic)',
        'option3': 'Text file with song list',
        'choose_option': 'Choose your option (1, 2 or 3): ',
        'invalid_option': 'Invalid option',
        'searching_xml': 'Automatic XML file search...',
        'xml_found': 'XML file found: {}',
        'xml_not_found': 'No XML file found in current directory.',
        'xml_files_searched': 'Files searched: {}',
        'playlist_url_prompt': 'Apple Music playlist URL: ',
        'text_file_prompt': 'Path to text file: ',
        'found_songs': 'Found {} songs to convert',
        'no_songs': '❌ No songs found',
        'playlist_name_prompt': 'Enter new playlist name: ',
        'connected_as': 'Connected as: {}',
        'playlist_created': 'Playlist created: {}',
        'searching': 'Searching ({}/{}): {}',
        'added': ' ✓ Added: {} - {}',
        'not_found': ' ✗ No results for: {}',
        'summary': '=== Summary ===',
        'found_added': 'Songs found and added: {}/{}',
        'not_found_tracks': 'Songs not found ({}):',
        'playlist_complete': 'Complete playlist: {}',
        'conversion_complete': '✅ Conversion complete! Playlist available: {}',
        'press_enter': 'Press Enter to quit...',
        'error_auth': 'Spotify authentication error: {}',
        'error_xml': 'Error reading XML file: {}',
        'error_playlist': 'Error creating playlist: {}',
        'error_unexpected': 'Unexpected error: {}',
        'error_details': 'Error details:',
        'auth_check': 'Check that:',
        'auth_check1': '1. Your CLIENT_ID and CLIENT_SECRET are correct',
        'auth_check2': '2. Redirect URL http://127.0.0.1:8888/callback is configured in your Spotify app',
        'auth_check3': '3. Your Spotify application is in \'Development\' mode',
        'env_error': 'Error: CLIENT_ID and CLIENT_SECRET must be defined in .env file',
        'env_help': 'Please create a .env file with:',
        'env_client_id': 'CLIENT_ID=your_spotify_client_id',
        'env_client_secret': 'CLIENT_SECRET=your_spotify_client_secret',
        'cannot_continue': 'Cannot continue without Spotify authentication',
        'xml_reading': 'Attempting to read XML file: {}',
        'xml_loaded': 'XML file loaded. Root: {}',
        'method1': 'Method 1: Searching for Name/Artist keys...',
        'name_keys_found': 'Name keys found: {}',
        'artist_keys_found': 'Artist keys found: {}',
        'found_song': 'Found: {}',
        'method2': 'Method 2: Searching all texts...',
        'strings_found': 'String elements found: {}',
        'text_found': 'Text found: {}',
        'method3': 'Method 3: Searching in dictionaries...',
        'dicts_found': 'Dict elements found: {}',
        'found_in_dict': 'Found in dict: {}',
        'total_songs': 'Total songs found: {}',
        'too_many_songs': 'Too many songs found ({}), limiting to 1000',
        'xml_parse_error': 'XML parsing error: {}',
        'xml_corrupted': 'XML file seems corrupted or malformed',
        'file_not_exists': 'Error: File {} does not exist',
        'not_xml_file': 'Warning: File {} does not seem to be an XML file',
        'text_songs_found': 'Found {} songs in text file',
        'text_error': 'Error reading text file: {}',
        'playlist_error': 'Error retrieving playlist: {}',
        'account_selection': '=== Spotify Account Selection ===',
        'current_account': 'Current account: {}',
        'change_account': 'Change account',
        'use_current': 'Use current account',
        'account_choice': 'Do you want to change Spotify account? (y/n): ',
        'logging_out': 'Logging out from current account...',
        'new_auth': 'Authenticating with new account...',
        'account_changed': 'Account changed successfully!',
        'logout_success': 'Logout successful.',
        'logout_error': 'Logout error: {}'
    }
}

def select_language():
    print("=== Language Selection / Sélection de langue ===")
    print("1. Français")
    print("2. English")
    while True:
        try:
            choice = input("Choose language / Choisissez la langue (1-2): ").strip()
            if choice == "1":
                return 'fr'
            elif choice == "2":
                return 'en'
            else:
                print("Invalid choice. Please enter 1 or 2.")
                print("Choix invalide. Veuillez entrer 1 ou 2.")
        except (EOFError, RuntimeError):
            # Fallback to French if stdin is not available
            print("Using French by default / Utilisation du français par défaut")
            return 'fr'

def logout_spotify():
    try:
        cache_file = os.path.expanduser("~/.cache/spotipy")
        if os.path.exists(cache_file):
            os.remove(cache_file)
            return True
        possible_cache_paths = [
            os.path.expanduser("~/.spotipy"),
            os.path.join(os.getcwd(), ".cache"),
            os.path.join(os.getcwd(), "spotipy_cache")
        ]
        for cache_path in possible_cache_paths:
            if os.path.exists(cache_path):
                if os.path.isfile(cache_path):
                    os.remove(cache_path)
                elif os.path.isdir(cache_path):
                    import shutil
                    shutil.rmtree(cache_path)
                return True
        return True
    except Exception as e:
        print(f"Erreur lors de la déconnexion: {e}")
        return False

def manage_spotify_account(lang='fr'):
    print(f"\n{LANGUAGES[lang]['account_selection']}")
    try:
        sp = authenticate_spotify(lang)
        if sp:
            try:
                current_user = sp.me()
                if current_user and 'display_name' in current_user:
                    print(f"{LANGUAGES[lang]['current_account']}".format(current_user['display_name']))
                else:
                    print(f"{LANGUAGES[lang]['current_account']}".format("Compte inconnu"))
            except Exception:
                print(f"{LANGUAGES[lang]['current_account']}".format("Compte inconnu"))
            change_choice = input(f"{LANGUAGES[lang]['account_choice']}" ).strip().lower()
            if change_choice in ['y', 'yes', 'o', 'oui']:
                print(LANGUAGES[lang]['logging_out'])
                if logout_spotify():
                    print(LANGUAGES[lang]['logout_success'])
                    print(LANGUAGES[lang]['new_auth'])
                    new_sp = authenticate_spotify(lang)
                    if new_sp:
                        try:
                            new_user = new_sp.me()
                            if new_user and 'display_name' in new_user:
                                print(f"{LANGUAGES[lang]['account_changed']}")
                                print(f"{LANGUAGES[lang]['current_account']}".format(new_user['display_name']))
                            else:
                                print(f"{LANGUAGES[lang]['account_changed']}")
                                print(f"{LANGUAGES[lang]['current_account']}".format("Nouveau compte"))
                        except Exception:
                            print(f"{LANGUAGES[lang]['account_changed']}")
                            print(f"{LANGUAGES[lang]['current_account']}".format("Nouveau compte"))
                        return new_sp
                    else:
                        print("Échec de la nouvelle authentification")
                        return None
                else:
                    print(LANGUAGES[lang]['logout_error'].format("Impossible de supprimer le cache"))
                    return sp
            else:
                return sp
        else:
            return authenticate_spotify(lang)
    except Exception as e:
        print(f"Erreur lors de la gestion du compte: {e}")
        return authenticate_spotify(lang)

def get_playlist_from_url(url):
    """Récupère les chansons depuis une URL de playlist Apple Music"""
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        artistDivs = soup.find_all('div', class_='songs-list-row__by-line')
        artists = []
        for content in artistDivs:
            txt = content.find('span', class_='svelte-x4tov2').text
            txt = txt.replace('\n', '').strip()
            artists.append(txt)
        songDivs = soup.find_all('div', class_='songs-list-row__song-name')
        songs = []
        for content in songDivs:
            txt = re.sub(r'\([^)]*\)', '', content.text).strip()
            songs.append(txt)
        search_array = []
        for i in range(0, min(len(artists), len(songs))):
            if artists[i] and songs[i]:
                search_array.append(f"{songs[i]} {artists[i]}")
        return search_array
    except Exception as e:
        print(f"Erreur lors de la récupération de la playlist: {e}")
        return []

def find_xml_file():
    current_dir = os.getcwd()
    possible_names = ['Library.xml', 'library.xml', 'Music Library.xml', 'iTunes Library.xml']
    for filename in possible_names:
        file_path = os.path.join(current_dir, filename)
        if os.path.exists(file_path):
            print(f"Fichier XML trouvé: {filename}")
            return file_path
    print("Aucun fichier XML trouvé dans le dossier courant.")
    print("Fichiers recherchés:", ", ".join(possible_names))
    return None

def get_songs_from_xml(xml_file_path=None, lang='fr'):
    try:
        if xml_file_path is None:
            xml_file_path = find_xml_file()
            if xml_file_path is None:
                return []
        print(LANGUAGES[lang]['xml_reading'].format(xml_file_path))
        if not os.path.exists(xml_file_path):
            print(LANGUAGES[lang]['file_not_exists'].format(xml_file_path))
            return []
        if not xml_file_path.lower().endswith('.xml'):
            print(LANGUAGES[lang]['not_xml_file'].format(xml_file_path))
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        print(LANGUAGES[lang]['xml_loaded'].format(root.tag))
        songs = []
        print(LANGUAGES[lang]['method1'])
        all_keys = root.findall('.//key')
        name_keys = []
        artist_keys = []
        for key in all_keys:
            if key.text == "Name":
                name_keys.append(key)
            elif key.text == "Artist":
                artist_keys.append(key)
        print(LANGUAGES[lang]['name_keys_found'].format(len(name_keys)))
        print(LANGUAGES[lang]['artist_keys_found'].format(len(artist_keys)))
        if name_keys and artist_keys:
            for name_key in name_keys:
                parent = None
                name_index = -1
                for elem in root.iter():
                    if name_key in elem:
                        parent = elem
                        children = list(parent)
                        try:
                            name_index = children.index(name_key)
                            break
                        except ValueError:
                            continue
                if parent is not None and name_index >= 0:
                    children = list(parent)
                    if name_index + 1 < len(children):
                        name_elem = children[name_index + 1]
                        if name_elem.text:
                            song_name = name_elem.text.strip()
                            artist_key = None
                            for child in parent:
                                if child.tag == 'key' and child.text == 'Artist':
                                    artist_key = child
                                    break
                            if artist_key is not None:
                                try:
                                    artist_index = children.index(artist_key)
                                    if artist_index + 1 < len(children):
                                        artist_elem = children[artist_index + 1]
                                        if artist_elem.text:
                                            artist_name = artist_elem.text.strip()
                                            song_name = re.sub(r'\([^)]*\)', '', song_name).strip()
                                            search_term = f"{song_name} {artist_name}"
                                            songs.append(search_term)
                                            print(LANGUAGES[lang]['found_song'].format(search_term))
                                except ValueError:
                                    continue
        if not songs:
            print(LANGUAGES[lang]['method2'])
            all_strings = root.findall('.//string')
            print(LANGUAGES[lang]['strings_found'].format(len(all_strings)))
            for string_elem in all_strings:
                if string_elem.text and len(string_elem.text.strip()) > 2:
                    text = string_elem.text.strip()
                    if not text.isdigit() and len(text) < 100:
                        songs.append(text)
                        print(LANGUAGES[lang]['text_found'].format(text))
        if not songs:
            print(LANGUAGES[lang]['method3'])
            dict_elements = root.findall('.//dict')
            print(LANGUAGES[lang]['dicts_found'].format(len(dict_elements)))
            for dict_elem in dict_elements:
                for i, child in enumerate(dict_elem):
                    if child.tag == 'key' and child.text in ['Name', 'Artist', 'Title']:
                        if i + 1 < len(dict_elem) and dict_elem[i + 1].tag == 'string':
                            text = dict_elem[i + 1].text
                            if text and len(text.strip()) > 2:
                                songs.append(text.strip())
                                print(LANGUAGES[lang]['found_in_dict'].format(text.strip()))
        print(LANGUAGES[lang]['total_songs'].format(len(songs)))
        if len(songs) > 1000:
            print(LANGUAGES[lang]['too_many_songs'].format(len(songs)))
            songs = songs[:1000]
        return songs
    except ET.ParseError as e:
        print(LANGUAGES[lang]['xml_parse_error'].format(e))
        print(LANGUAGES[lang]['xml_corrupted'])
        return []
    except Exception as e:
        print(LANGUAGES[lang]['error_xml'].format(e))
        print(LANGUAGES[lang]['error_details'])
        traceback.print_exc()
        return []

def get_songs_from_text_file(text_file_path, lang='fr'):
    try:
        with open(text_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        songs = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                songs.append(line)
        print(LANGUAGES[lang]['text_songs_found'].format(len(songs)))
        return songs
    except Exception as e:
        print(LANGUAGES[lang]['text_error'].format(e))
        return []

def authenticate_spotify(lang='fr'):
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    if not CLIENT_ID or not CLIENT_SECRET:
        print(LANGUAGES[lang]['env_error'])
        print(LANGUAGES[lang]['env_help'])
        print(LANGUAGES[lang]['env_client_id'])
        print(LANGUAGES[lang]['env_client_secret'])
        return None
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri='http://127.0.0.1:8888/callback',
            scope='playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-read user-library-modify user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing'
        ))
        return sp
    except Exception as e:
        print(LANGUAGES[lang]['error_auth'].format(e))
        print(LANGUAGES[lang]['auth_check'])
        print(LANGUAGES[lang]['auth_check1'])
        print(LANGUAGES[lang]['auth_check2'])
        print(LANGUAGES[lang]['auth_check3'])
        return None

def search_and_add(sp, search_array, lang='fr'):
    if not sp:
        print(LANGUAGES[lang]['cannot_continue'])
        return None
    try:
        username = sp.me()['id']
        print(LANGUAGES[lang]['connected_as'].format(sp.me()['display_name']))
        playlist_name = input(LANGUAGES[lang]['playlist_name_prompt'])
        playlist = sp.user_playlist_create(username, playlist_name, public=False, description='Créée avec Python')
        playlist_id = playlist['id']
        playlist_url = playlist['external_urls']['spotify']
        print(LANGUAGES[lang]['playlist_created'].format(playlist_url))
        found_tracks = 0
        not_found_tracks = []
        for i, search_term in enumerate(search_array):
            print(LANGUAGES[lang]['searching'].format(i+1, len(search_array), search_term))
            results = sp.search(q=search_term, limit=1, type='track')
            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                sp.user_playlist_add_tracks(username, playlist_id, [track['uri']])
                print(LANGUAGES[lang]['added'].format(track['name'], track['artists'][0]['name']))
                found_tracks += 1
            else:
                print(LANGUAGES[lang]['not_found'].format(search_term))
                not_found_tracks.append(search_term)
        print(LANGUAGES[lang]['summary'])
        print(LANGUAGES[lang]['found_added'].format(found_tracks, len(search_array)))
        if not_found_tracks:
            print(LANGUAGES[lang]['not_found_tracks'].format(len(not_found_tracks)))
            for track in not_found_tracks:
                print(f"  - {track}")
        print(LANGUAGES[lang]['playlist_complete'].format(playlist_url))
        return playlist_url
    except Exception as e:
        print(LANGUAGES[lang]['error_playlist'].format(e))
        return None

def print_progress_bar(iteration, total):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(25 * iteration // total)
    bar = '█' * filledLength + '-' * (25 - filledLength)
    print('\r%s |%s| %s%% %s' % ('Progression:', bar, percent, 'Terminé'), end='\r')
    if iteration == total:
        print()

def main():
    lang = 'fr'  # Default language
    try:
        lang = select_language()
        print(LANGUAGES[lang]['title'])
        print("1.", LANGUAGES[lang]['option1'])
        print("2.", LANGUAGES[lang]['option2'])
        print("3.", LANGUAGES[lang]['option3'])
        
        try:
            choice = input(f"\n{LANGUAGES[lang]['choose_option']}" ).strip()
        except (EOFError, RuntimeError):
            print("Error reading input. Please run the program in a console.")
            print("Erreur de lecture. Veuillez exécuter le programme dans une console.")
            return
            
        sp = manage_spotify_account(lang)
        if not sp:
            try:
                input(LANGUAGES[lang]['press_enter'])
            except (EOFError, RuntimeError):
                pass
            return
        search_array = []
        if choice == "1":
            try:
                url = input(LANGUAGES[lang]['playlist_url_prompt'])
                search_array = get_playlist_from_url(url)
            except (EOFError, RuntimeError):
                print("Error reading URL input.")
                return
        elif choice == "2":
            print("Veuillez placer votre fichier Library.xml (ou Music Library.xml, iTunes Library.xml) dans le même dossier que ce script.")
            try:
                input("Appuyez sur Entrée quand c'est fait...")
            except (EOFError, RuntimeError):
                pass
            search_array = get_songs_from_xml(None, lang)
        elif choice == "3":
            try:
                text_path = input(LANGUAGES[lang]['text_file_prompt'])
                search_array = get_songs_from_text_file(text_path, lang)
            except (EOFError, RuntimeError):
                print("Error reading file path input.")
                return
        else:
            print(LANGUAGES[lang]['invalid_option'])
            try:
                input(LANGUAGES[lang]['press_enter'])
            except (EOFError, RuntimeError):
                pass
            return
        if search_array:
            print(LANGUAGES[lang]['found_songs'].format(len(search_array)))
            result = search_and_add(sp, search_array, lang)
            if result:
                print(LANGUAGES[lang]['conversion_complete'].format(result))
        else:
            print(LANGUAGES[lang]['no_songs'])
        try:
            input(f"\n{LANGUAGES[lang]['press_enter']}")
        except (EOFError, RuntimeError):
            pass
    except Exception as e:
        print(LANGUAGES[lang]['error_unexpected'].format(e))
        print(LANGUAGES[lang]['error_details'])
        traceback.print_exc()
        try:
            input(LANGUAGES[lang]['press_enter'])
        except (EOFError, RuntimeError):
            pass

if __name__ == "__main__":
    main()
