from exceptions import NavigationError, MissionDataError, TrajectoireError, CarburantError
import re

def valider_mission(mission_dict):
    """Valide les données d'une mission spatiale."""
    champs_obligatoires = ["id", "nom", "destination", "date_lancement", "duree_jours", "budget_millions_usd"]
    
    # 1. Vérifier les champs présents
    for champ in champs_obligatoires:
        if champ not in mission_dict:
            raise MissionDataError(f"Champ obligatoire manquant : {champ}")
    
    # 2. Vérifier si les valeurs numériques sont positives
    if mission_dict["duree_jours"] <= 0:
        raise MissionDataError("La durée de la mission doit être positive.")
    
    if mission_dict["budget_millions_usd"] <= 0:
        raise MissionDataError("Le budget doit être un nombre positif.")
    
    # 3. Vérifier le format de la date (AAAA-MM-JJ)
    if not re.match(r"\d{4}-\d{2}-\d{2}", mission_dict["date_lancement"]):
        raise MissionDataError("La date de lancement doit être au format AAAA-MM-JJ.")
    
    # 4. Vérification de cohérence (exemple simple)
    # Si destination est Mars, la durée doit être réaliste (ex: > 150 jours)
    if mission_dict["destination"] == "Mars" and mission_dict["duree_jours"] < 150:
        raise TrajectoireError("Durée de trajet impossible pour Mars (min. 150 jours).")
        
    return True

def verifier_carburant(releve):
    """Vérifie le niveau de carburant et lève une alerte si critique."""
    pct = releve["carburant_pct"]
    if pct < 10:
        raise CarburantError(f"CRITIQUE : Carburant à {pct}% ! Abandon de mission imminent.")
    elif pct < 30:
        print(f" ATTENTION : Niveau de carburant bas ({pct}%).")

# Cas 1 : Mission Valide
print("--- Test 1 : Mission valide ---")
m1 = {
    "id": "MSN-999", "nom": "Test Alpha", "destination": "Lune",
    "date_lancement": "2028-05-12", "duree_jours": 15, "budget_millions_usd": 500
}
try:
    if valider_mission(m1): print(" Données de mission valides.")
except NavigationError as e:
    print(f" Erreur : {e}")

# Cas 2 : Durée négative
print("\n--- Test 2 : Durée négative ---")
m2 = m1.copy()
m2["duree_jours"] = -10
try:
    valider_mission(m2)
except NavigationError as e:
    print(f" {type(e).__name__} : {e}")

# Cas 3 : Trajectoire impossible pour Mars
print("\n--- Test 3 : Trajectoire Mars trop courte ---")
m3 = m1.copy()
m3["destination"] = "Mars"
m3["duree_jours"] = 50
try:
    valider_mission(m3)
except NavigationError as e:
    print(f" {type(e).__name__} : {e}")

# Cas 4 : Carburant critique
print("\n--- Test 4 : Carburant critique ---")
try:
    verifier_carburant({"carburant_pct": 5.2})
except CarburantError as e:
    print(f" {e}")

