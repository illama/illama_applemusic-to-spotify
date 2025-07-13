# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Support des releases GitHub avec fichiers .exe
- Workflow GitHub Actions automatisé
- Script de build automatique (`build_exe.py`)
- Documentation complète pour les releases
- Guide de configuration Spotify détaillé

### Changed
- Amélioration de la documentation
- Optimisation du processus de build

## [1.0.0] - 2024-01-15

### Added
- Conversion de playlists Apple Music vers Spotify
- Support des fichiers XML exportés d'Apple Music
- Import depuis des fichiers texte
- Interface bilingue (français/anglais)
- Gestion multi-comptes Spotify
- Détection automatique du fichier Library.xml
- Gestion des erreurs et messages informatifs

### Features
- **Option 1** : Conversion via URL de playlist Apple Music
- **Option 2** : Import automatique depuis un fichier XML
- **Option 3** : Import depuis un fichier texte avec liste de chansons
- Changement de compte Spotify à la volée
- Recherche intelligente des chansons sur Spotify
- Création de playlists privées ou publiques
- Barre de progression pour le suivi des conversions

### Technical
- Utilisation de l'API Spotify Web
- Parsing XML robuste pour les exports Apple Music
- Gestion des tokens d'authentification
- Support des encodages UTF-8
- Gestion des erreurs réseau et API

---

## Types de changements

- **Added** : Nouvelles fonctionnalités
- **Changed** : Modifications de fonctionnalités existantes
- **Deprecated** : Fonctionnalités qui seront supprimées
- **Removed** : Fonctionnalités supprimées
- **Fixed** : Corrections de bugs
- **Security** : Corrections de vulnérabilités

## Notes de version

### Version 1.0.0
- Première version stable
- Toutes les fonctionnalités principales implémentées
- Documentation complète
- Support des releases GitHub avec .exe

### Prochaines versions prévues
- **v1.1.0** : Optimisations de performance
- **v1.2.0** : Interface graphique optionnelle
- **v2.0.0** : Support d'autres plateformes (Deezer, YouTube Music) 