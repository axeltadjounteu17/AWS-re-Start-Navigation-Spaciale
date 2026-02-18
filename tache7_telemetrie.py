import json
from datetime import datetime

# 1. Charger les données
with open('mission_data/telemetrie.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

releves = data['releves']

# 2. Affichage du tableau résumé
print(f"{"Phase":<20} | {"Altitude":<15} | {"Vitesse":<10} | {"Carburant":<10} | {"Alertes"}")
print("-" * 80)

alertes_detectees = []

for r in releves:
    # Extraire les alertes (systèmes non nominaux)
    alertes = [sys for sys, etat in r['systemes'].items() if etat != "nominal"]
    alerte_str = ", ".join(alertes) if alertes else "-"
    
    if alertes:
        alertes_detectees.append({
            "timestamp": r['timestamp'],
            "phase": r['phase'],
            "alertes": r['systemes']
        })
    
    # Formatage de l'altitude pour plus de lisibilité
    alt = f"{r['altitude_km']:,} km".replace(",", " ")
    
    print(f"{r['phase']:<20} | {alt:<15} | {r['vitesse_km_s']:<10} | {r['carburant_pct']}%{'':<3} | {alerte_str}")


if len(releves) >= 2:
    # Premier et dernier relevé
    first = releves[0]
    last = releves[-1]
    
    # Parsing des dates
    d1 = datetime.strptime(first['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
    d2 = datetime.strptime(last['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
    
    # Différence de temps en jours
    delta_jours = (d2 - d1).days
    
    # Différence de carburant
    conso_totale = first['carburant_pct'] - last['carburant_pct']
    
    if delta_jours > 0:
        conso_moyenne = conso_totale / delta_jours
        print(f"Consommation totale : {conso_totale:.1f}%")
        print(f"Durée totale : {delta_jours} jours")
        print(f" Consommation moyenne : {conso_moyenne:.3f}% / jour")
    else:
        print("La durée est trop courte pour calculer une moyenne journalière.")

import os
os.makedirs('mission_data/rapports', exist_ok=True)

with open('mission_data/rapports/alertes_systemes.json', 'w', encoding='utf-8') as f:
    json.dump(alertes_detectees, f, indent=2, ensure_ascii=False)

print(f" {len(alertes_detectees)} alertes sauvegardées dans 'mission_data/rapports/alertes_systemes.json'.")

