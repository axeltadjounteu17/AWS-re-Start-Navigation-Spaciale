Navigation Spatiale — Centre de Contrôle

Ce projet est une simulation complète d'un système de gestion de missions spatiales développé en Python. Il a été conçu pour démontrer la maîtrise des concepts fondamentaux de la programmation à travers des tâches concrètes de navigation interplanétaire.

Fonctionnalités clés
- Gestion de Bord : Lecture et filtrage automatique des journaux de bord.
- Analyse de Télémétrie : Suivi en temps réel de l'état des vaisseaux (carburant, altitude, vitesse).
- Calculateur de Navigation : Module dédié au calcul des distances et des durées de trajet entre les planètes.
- Centre de Contrôle Interactif : Une interface console pour piloter toutes les opérations de la mission.

Notions techniques couvertes
- Manipulation de fichiers (TEXTE, JSON)
- Gestion robuste des erreurs (Exceptions personnalisées)
- Programmation modulaire (Création de packages utilitaires)
- Automatisation avec le module `os`

 Structure du projet
- `centre_controle.py` : Le programme principal (le tableau de bord).
- `navigation.py` : Les algorithmes de calcul spatial.
- `mission_data/` : Base de données du projet (missions, télémétrie, archives).
