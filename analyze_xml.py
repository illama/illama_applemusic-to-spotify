#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour analyser la structure d'un fichier XML exporté d'Apple Music
"""

import xml.etree.ElementTree as ET
import sys

def analyze_xml_structure(xml_file_path):
    """Analyse la structure du fichier XML pour comprendre le format"""
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        print(f"=== Analyse du fichier XML: {xml_file_path} ===")
        print(f"Racine: {root.tag}")
        print(f"Attributs de la racine: {root.attrib}")
        
        # Analyser les premiers niveaux
        print(f"\n=== Structure des premiers niveaux ===")
        for i, child in enumerate(root[:10]):  # Afficher les 10 premiers enfants
            print(f"{i+1}. {child.tag}: {child.attrib}")
            if child.text and child.text.strip():
                print(f"   Texte: {child.text.strip()[:100]}...")
        
        # Chercher les éléments de chansons
        print(f"\n=== Recherche d'éléments de chansons ===")
        
        # Chercher les clés "Name" et "Artist"
        name_keys = root.findall('.//key[text()="Name"]')
        artist_keys = root.findall('.//key[text()="Artist"]')
        
        print(f"Clés 'Name' trouvées: {len(name_keys)}")
        print(f"Clés 'Artist' trouvées: {len(artist_keys)}")
        
        if name_keys:
            print(f"\nPremiers noms de chansons trouvés:")
            for i, name_key in enumerate(name_keys[:5]):
                next_elem = name_key.getnext()
                if next_elem is not None and next_elem.text:
                    print(f"  {i+1}. {next_elem.text}")
        
        if artist_keys:
            print(f"\nPremiers artistes trouvés:")
            for i, artist_key in enumerate(artist_keys[:5]):
                next_elem = artist_key.getnext()
                if next_elem is not None and next_elem.text:
                    print(f"  {i+1}. {next_elem.text}")
        
        # Chercher les dictionnaires (format iTunes)
        dict_elements = root.findall('.//dict')
        print(f"\nÉléments 'dict' trouvés: {len(dict_elements)}")
        
        # Analyser quelques dictionnaires
        if dict_elements:
            print(f"\nAnalyse des premiers dictionnaires:")
            for i, dict_elem in enumerate(dict_elements[:3]):
                print(f"\nDictionnaire {i+1}:")
                for j, child in enumerate(dict_elem[:10]):  # Afficher les 10 premiers enfants
                    print(f"  {j+1}. {child.tag}: {child.text if child.text else 'None'}")
        
        # Chercher tous les textes
        all_strings = root.findall('.//string')
        print(f"\nÉléments 'string' trouvés: {len(all_strings)}")
        
        if all_strings:
            print(f"\nPremiers textes trouvés:")
            for i, string_elem in enumerate(all_strings[:10]):
                if string_elem.text and len(string_elem.text.strip()) > 2:
                    print(f"  {i+1}. {string_elem.text.strip()}")
        
        return True
        
    except Exception as e:
        print(f"Erreur lors de l'analyse du fichier XML: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_xml.py <chemin_vers_fichier_xml>")
        print("Exemple: python analyze_xml.py library.xml")
        return
    
    xml_file_path = sys.argv[1]
    analyze_xml_structure(xml_file_path)

if __name__ == "__main__":
    main() 