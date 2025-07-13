#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test simple pour vérifier la lecture d'un fichier XML
"""

import xml.etree.ElementTree as ET
import os
import sys

def test_xml_file(xml_file_path):
    """Test simple de lecture d'un fichier XML"""
    try:
        print(f"=== Test de lecture du fichier XML ===")
        print(f"Fichier: {xml_file_path}")
        
        # Vérifier que le fichier existe
        if not os.path.exists(xml_file_path):
            print(f"❌ Erreur: Le fichier {xml_file_path} n'existe pas")
            return False
        
        # Vérifier la taille du fichier
        file_size = os.path.getsize(xml_file_path)
        print(f"Taille du fichier: {file_size} octets")
        
        if file_size == 0:
            print("❌ Erreur: Le fichier est vide")
            return False
        
        # Essayer de parser le XML
        print("Tentative de parsing XML...")
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        print(f"✅ XML parsé avec succès!")
        print(f"Racine: {root.tag}")
        print(f"Nombre d'éléments enfants: {len(root)}")
        
        # Afficher les premiers éléments
        print(f"\nPremiers éléments:")
        for i, child in enumerate(root[:5]):
            print(f"  {i+1}. {child.tag}")
        
        # Chercher des éléments de chansons
        print(f"\nRecherche d'éléments de chansons...")
        
        # Chercher les clés "Name"
        name_keys = root.findall('.//key[text()="Name"]')
        print(f"Clés 'Name' trouvées: {len(name_keys)}")
        
        # Chercher les clés "Artist"
        artist_keys = root.findall('.//key[text()="Artist"]')
        print(f"Clés 'Artist' trouvées: {len(artist_keys)}")
        
        # Chercher tous les éléments string
        all_strings = root.findall('.//string')
        print(f"Éléments 'string' trouvés: {len(all_strings)}")
        
        # Afficher quelques exemples
        if all_strings:
            print(f"\nExemples de textes trouvés:")
            for i, string_elem in enumerate(all_strings[:10]):
                if string_elem.text and len(string_elem.text.strip()) > 2:
                    print(f"  {i+1}. {string_elem.text.strip()}")
        
        print(f"\n✅ Test terminé avec succès!")
        return True
        
    except ET.ParseError as e:
        print(f"❌ Erreur de parsing XML: {e}")
        print("Le fichier XML semble corrompu ou mal formaté")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_xml.py <chemin_vers_fichier_xml>")
        print("Exemple: python test_xml.py library.xml")
        input("Appuyez sur Entrée pour quitter...")
        return
    
    xml_file_path = sys.argv[1]
    success = test_xml_file(xml_file_path)
    
    if success:
        print("\n✅ Le fichier XML peut être lu correctement!")
    else:
        print("\n❌ Problème avec le fichier XML")
    
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main() 