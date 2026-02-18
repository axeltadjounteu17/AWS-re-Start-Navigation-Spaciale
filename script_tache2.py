# --- script_tache2_exploration.py ---
"""
OBJECTIF : Explorer les dossiers et fichiers avec le module 'os'.
"""

import os

dossier = "mission_data"

# 1. Vérifier si le dossier existe
if os.path.exists(dossier):
    print(f"📂 Exploration de {dossier}/")
    
    # 2. Lister les fichiers et afficher leur taille
    for fichier in os.listdir(dossier):
        chemin = os.path.join(dossier, fichier)
        if os.path.isfile(chemin):
            taille_ko = os.path.getsize(chemin) / 1024
            print(f"   📄 {fichier:<20} ({taille_ko:.1f} Ko)")

    # 3. Créer des sous-dossiers s'ils n'existent pas
    for s_dossier in ["rapports", "archives"]:
        chemin_sd = os.path.join(dossier, s_dossier)
        if not os.path.exists(chemin_sd):
            os.makedirs(chemin_sd)
            print(f"   📁 {s_dossier}/ [créé]")
else:
    print(f"❌ Erreur : Le dossier {dossier} n'existe pas.")
