# --- script_tache1_journal.py ---
"""
OBJECTIF : Lire le journal de bord et isoler les alertes.
"""

input_file = "mission_data/journal_bord.txt"
output_file = "mission_data/alertes.txt"

# 1. Lire toutes les lignes
with open(input_file, 'r', encoding='utf-8') as f:
    lignes = f.readlines()

print(f"Journal de bord : {len(lignes)} entrées")
print("--- Alertes détectées ---")

lignes_alertes = []

# 2. Filtrer les lignes contenant "alerte" (en minuscules ou majuscules)
for line in lignes:
    if "alerte" in line.lower():
        print(line.strip())
        lignes_alertes.append(line)

# 3. Sauvegarder dans un nouveau fichier
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(lignes_alertes)

print(f"✅ Fichier {output_file} créé avec {len(lignes_alertes)} alertes.")
