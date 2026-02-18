# --- script_tache3_json_missions.py ---
"""
OBJECTIF : Lire un fichier JSON et calculer des statistiques simples.
"""

import json

with open("mission_data/missions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

missions = data["missions"]
budget_total = 0

print(f"{'ID':<10} | {'Nom':<15} | {'Destination':<10} | {'Budget (M$)'}")
print("-" * 50)

for m in missions:
    print(f"{m['id']:<10} | {m['nom']:<15} | {m['destination']:<10} | {m['budget_millions_usd']}")
    budget_total += m["budget_millions_usd"]

print("-" * 50)
print(f"Budget total des missions : {budget_total} millions de $")
