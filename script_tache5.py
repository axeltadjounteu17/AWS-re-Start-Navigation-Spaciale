# --- script_tache5_os_avance.py ---
"""
OBJECTIF : Archivage et informations système.
"""

import os
import shutil
from datetime import datetime

# 1. Créer un nom de fichier avec la date d'aujourd'hui
date_du_jour = datetime.now().strftime("%Y-%m-%d")
source = "mission_data/journal_bord.txt"
destination = f"mission_data/archives/journal_bord_{date_du_jour}.txt"

# 2. Copier le fichier vers les archives
try:
    shutil.copy(source, destination)
    print(f"✅ Journal archivé dans : {destination}")
except FileNotFoundError:
    print("❌ Fichier source introuvable.")

# 3. Récupérer le dossier actuel
print(f"🏠 Dossier de travail actuel : {os.getcwd()}")
