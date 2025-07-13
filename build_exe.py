#!/usr/bin/env python3
"""
Script de build pour créer un fichier .exe du convertisseur Apple Music vers Spotify
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def clean_build_dirs():
    """Nettoie les dossiers de build précédents"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"Suppression du dossier {dir_name}...")
            shutil.rmtree(dir_name)
    
    # Nettoyer les fichiers .spec
    for spec_file in Path('.').glob('*.spec'):
        print(f"Suppression du fichier {spec_file}...")
        spec_file.unlink()

def build_exe():
    """Construit le fichier .exe avec PyInstaller"""
    print("=== Construction du fichier .exe ===")
    
    # Commande PyInstaller
    cmd = [
        'pyinstaller',
        '--onefile',                    # Un seul fichier .exe
        # '--windowed',                 # Pas de console (optionnel, retirez si vous voulez garder la console)
        '--name=AppleMusic-to-Spotify', # Nom du fichier .exe
        '--icon=icon.ico',              # Icône (optionnel, retirez si pas d'icône)
        '--add-data=config.env;.',      # Inclure le fichier de config
        '--hidden-import=spotipy',
        '--hidden-import=spotipy.oauth2',
        '--hidden-import=requests',
        '--hidden-import=bs4',
        '--hidden-import=dotenv',
        'index.py'
    ]
    
    # Retirer l'icône si elle n'existe pas
    if not os.path.exists('icon.ico'):
        cmd.remove('--icon=icon.ico')
    
    # Retirer --windowed si vous voulez garder la console
    # cmd.remove('--windowed')
    
    print("Commande PyInstaller:", ' '.join(cmd))
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Build réussi!")
        print("Sortie:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erreur lors du build:")
        print("Erreur:", e.stderr)
        return False

def create_release_package():
    """Crée un package de release avec les fichiers nécessaires"""
    print("\n=== Création du package de release ===")
    
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # Copier le .exe
    exe_path = "dist/AppleMusic-to-Spotify.exe"
    if os.path.exists(exe_path):
        shutil.copy2(exe_path, release_dir)
        print(f"✅ {exe_path} copié vers {release_dir}")
    else:
        print(f"❌ {exe_path} non trouvé")
        return False
    
    # Copier les fichiers de documentation
    docs_to_copy = ['README.md', 'SETUP.md', '.env-example']
    for doc in docs_to_copy:
        if os.path.exists(doc):
            shutil.copy2(doc, release_dir)
            print(f"✅ {doc} copié vers {release_dir}")
    
    # Créer un fichier .env-example dans le release
    env_example_content = """# Configuration Spotify
# Obtenez ces valeurs sur https://developer.spotify.com/dashboard
CLIENT_ID=votre_client_id_ici
CLIENT_SECRET=votre_client_secret_ici
"""
    with open(os.path.join(release_dir, 'config.env'), 'w', encoding='utf-8') as f:
        f.write(env_example_content)
    print("✅ config.env créé dans le release")
    
    print(f"\n🎉 Package de release créé dans le dossier '{release_dir}'")
    print("Fichiers inclus:")
    for file in os.listdir(release_dir):
        print(f"  - {file}")
    
    return True

def main():
    print("=== Script de build pour Apple Music to Spotify Converter ===")
    
    # Vérifier que PyInstaller est installé
    try:
        import PyInstaller
        print("✅ PyInstaller est installé")
    except ImportError:
        print("❌ PyInstaller n'est pas installé")
        print("Installez-le avec: pip install pyinstaller")
        return False
    
    # Nettoyer les builds précédents
    clean_build_dirs()
    
    # Construire le .exe
    if not build_exe():
        return False
    
    # Créer le package de release
    if not create_release_package():
        return False
    
    print("\n🎉 Build terminé avec succès!")
    print("Le fichier .exe se trouve dans le dossier 'release'")
    print("Vous pouvez maintenant créer une release GitHub avec ce dossier")

if __name__ == "__main__":
    main() 