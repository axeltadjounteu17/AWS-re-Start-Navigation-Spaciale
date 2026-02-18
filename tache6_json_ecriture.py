import json
import os

def ajouter_mission(chemin_json, nouvelle_mission):
    """Ajoute une nouvelle mission au fichier JSON s'il l'ID n'existe pas déjà."""
    # 1. Charger les missions existantes
    with open(chemin_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Vérifier si l'ID existe déjà
    for m in data['missions']:
        if m['id'] == nouvelle_mission['id']:
            raise ValueError(f"L'ID {nouvelle_mission['id']} existe déjà !")
    
    # 3. Ajouter la mission
    data['missions'].append(nouvelle_mission)
    
    # 4. Sauvegarder le fichier avec une belle indentation
    with open(chemin_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f" Mission '{nouvelle_mission['nom']}' ajoutée avec succès.")

def supprimer_mission(chemin_json, mission_id):
    """Supprime une mission par son ID après confirmation."""
    with open(chemin_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    initial_count = len(data['missions'])
    data['missions'] = [m for m in data['missions'] if m['id'] != mission_id]
    
    if len(data['missions']) < initial_count:
        with open(chemin_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f" Mission {mission_id} supprimée.")
    else:
        print(f" Aucune mission trouvée avec l'ID {mission_id}.")

chemin = "mission_data/missions.json"

nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}

try:
    ajouter_mission(chemin, nouvelle)
except ValueError as e:
    print(f" Erreur : {e}")

# On peut tester en supprimant la mission qu'on vient d'ajouter ou une autre
supprimer_mission(chemin, "MSN-006")

