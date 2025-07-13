#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de diagnostic pour analyser en détail la structure d'un fichier XML
"""

import xml.etree.ElementTree as ET
import os
import sys

def diagnose_xml_structure(xml_file_path):
    """Analyse détaillée de la structure du fichier XML"""
    try:
        print(f"=== Diagnostic du fichier XML ===")
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
        
        # Analyser la structure générale
        print(f"\n=== Structure générale ===")
        element_counts = {}
        for elem in root.iter():
            tag = elem.tag
            element_counts[tag] = element_counts.get(tag, 0) + 1
        
        print("Éléments trouvés:")
        for tag, count in sorted(element_counts.items()):
            print(f"  {tag}: {count}")
        
        # Chercher spécifiquement les éléments de chansons
        print(f"\n=== Recherche d'éléments de chansons ===")
        
        # Chercher tous les éléments 'key'
        all_keys = root.findall('.//key')
        print(f"Éléments 'key' trouvés: {len(all_keys)}")
        
        # Analyser le contenu des clés
        key_contents = {}
        for key in all_keys:
            if key.text:
                content = key.text
                key_contents[content] = key_contents.get(content, 0) + 1
        
        print(f"\nContenu des clés trouvées:")
        for content, count in sorted(key_contents.items()):
            print(f"  '{content}': {count}")
        
        # Chercher les éléments 'string'
        all_strings = root.findall('.//string')
        print(f"\nÉléments 'string' trouvés: {len(all_strings)}")
        
        # Analyser quelques exemples de textes
        if all_strings:
            print(f"\nExemples de textes (premiers 20):")
            for i, string_elem in enumerate(all_strings[:20]):
                if string_elem.text and len(string_elem.text.strip()) > 2:
                    print(f"  {i+1}. '{string_elem.text.strip()}'")
        
        # Chercher les éléments 'dict'
        all_dicts = root.findall('.//dict')
        print(f"\nÉléments 'dict' trouvés: {len(all_dicts)}")
        
        # Analyser la structure des premiers dictionnaires
        if all_dicts:
            print(f"\nStructure des premiers dictionnaires:")
            for i, dict_elem in enumerate(all_dicts[:3]):
                print(f"\nDictionnaire {i+1}:")
                for j, child in enumerate(dict_elem[:10]):  # Afficher les 10 premiers enfants
                    print(f"  {j+1}. {child.tag}: '{child.text if child.text else 'None'}'")
        
        # Chercher des patterns spécifiques
        print(f"\n=== Recherche de patterns spécifiques ===")
        
        # Chercher les éléments qui pourraient contenir des chansons
        potential_songs = []
        for string_elem in all_strings:
            if string_elem.text and len(string_elem.text.strip()) > 2:
                text = string_elem.text.strip()
                # Filtrer les textes qui ressemblent à des noms de chansons
                if (not text.isdigit() and 
                    len(text) < 100 and 
                    not text.startswith('http') and
                    not text.startswith('file://')):
                    potential_songs.append(text)
        
        print(f"Textes potentiellement des chansons trouvés: {len(potential_songs)}")
        if potential_songs:
            print(f"\nExemples de chansons potentielles:")
            for i, song in enumerate(potential_songs[:10]):
                print(f"  {i+1}. {song}")
        
        print(f"\n✅ Diagnostic terminé avec succès!")
        return True
        
    except ET.ParseError as e:
        print(f"❌ Erreur de parsing XML: {e}")
        print("Le fichier XML semble corrompu ou mal formaté")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python diagnose_xml.py <chemin_vers_fichier_xml>")
        print("Exemple: python diagnose_xml.py Library.xml")
        input("Appuyez sur Entrée pour quitter...")
        return
    
    xml_file_path = sys.argv[1]
    success = diagnose_xml_structure(xml_file_path)
    
    if success:
        print("\n✅ Le fichier XML a été analysé avec succès!")
        print("Utilisez ces informations pour comprendre la structure de votre fichier.")
    else:
        print("\n❌ Problème avec l'analyse du fichier XML")
    
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main() 