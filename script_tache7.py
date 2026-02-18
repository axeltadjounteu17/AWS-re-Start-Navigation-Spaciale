# --- script_tache7_telemetrie.py ---
"""
OBJECTIF : Analyser les données de vol et les alertes.
EXPLICATION : On parcourt une liste de relevés techniques pour trouver les problèmes.
"""

import json

# Charger les données de télémétrie
with open('mission_data/telemetrie.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Analyse du vaisseau : {data['vaisseau']}")
print("-" * 30)

# Parcourir chaque relevé
for r in data['releves']:
    phase = r['phase']
    carburant = r['carburant_pct']
    
    # Chercher si un système n'est pas "nominal" (pas normal)
    alertes = []
    for systeme, etat in r['systemes'].items():
        if etat != "nominal":
            alertes.append(systeme)
    
    # Affichage simple
    alerte_msg = f" [ALERTES: {', '.join(alertes)}]" if alertes else ""
    print(f"Phase: {phase:<20} | Carburant: {carburant}% {alerte_msg}")
