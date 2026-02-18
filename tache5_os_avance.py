import os
import shutil             # Pour copier des fichiers
from datetime import date  # Pour obtenir la date du jour

# Date du jour au format YYYY-MM-DD
date_jour = date.today().strftime("%Y-%m-%d")
print(f"Date du jour : {date_jour}")

# Construire les chemins avec os.path.join() pour que ça marche sur tous les OS
chemin_source = os.path.join("mission_data", "journal_bord.txt")
nom_archive = f"journal_bord_{date_jour}.txt"
chemin_destination = os.path.join("mission_data", "archives", nom_archive)

# Vérifier que le dossier archives existe, sinon le créer
os.makedirs(os.path.join("mission_data", "archives"), exist_ok=True)

# Copier le fichier avec shutil.copy()
shutil.copy(chemin_source, chemin_destination)
print(f" Copie effectuée : {chemin_source} → {chemin_destination}")

# Créer le dossier rapports s'il n'existe pas
os.makedirs(os.path.join("mission_data", "rapports"), exist_ok=True)

# Construire le chemin du rapport
chemin_rapport = os.path.join("mission_data", "rapports", "rapport_systeme.txt")

with open(chemin_rapport, "w", encoding="utf-8") as rapport:
    # 1. Répertoire de travail actuel
    rapport.write(f"=== RAPPORT SYSTÈME ===\n")
    rapport.write(f"Date : {date_jour}\n\n")
    rapport.write(f"Répertoire de travail : {os.getcwd()}\n\n")
    
    # 2. Variables d'environnement liées à Python ou PATH
    rapport.write("Variables d'environnement (PYTHON / PATH) :\n")
    for cle, valeur in os.environ.items():
        if "PYTHON" in cle.upper() or "PATH" in cle.upper():
            rapport.write(f"  {cle} = {valeur}\n")
    
    # 3. Espace disque (bonus)
    rapport.write("\nEspace disque :\n")
    usage = shutil.disk_usage("/")
    rapport.write(f"  Total  : {usage.total / (1024**3):.1f} Go\n")
    rapport.write(f"  Utilisé: {usage.used / (1024**3):.1f} Go\n")
    rapport.write(f"  Libre  : {usage.free / (1024**3):.1f} Go\n")

print(f" Rapport système créé : {chemin_rapport}")

# Afficher un résumé
print("\n=== RÉSUMÉ DES OPÉRATIONS ===")
print(f"1. Archive créée     : {chemin_destination}")
print(f"2. Rapport créé      : {chemin_rapport}")

# Vérifier que les fichiers existent
print(f"\nVérification :")
print(f"  Archive existe ? {os.path.exists(chemin_destination)}")
print(f"  Rapport existe ? {os.path.exists(chemin_rapport)}")

