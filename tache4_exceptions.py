import json

def charger_json_securise(chemin):
    """
    Charge un fichier JSON de manière sécurisée.
    Gère les erreurs : fichier inexistant, JSON mal formé, fichier vide.
    Retourne les données si tout va bien, None sinon.
    """
    try:
        # Tenter d'ouvrir le fichier
        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
        
        # Vérifier si le fichier est vide
        if len(contenu.strip()) == 0:
            print(f" Le fichier {chemin} est vide.")
            return None
        
        # Tenter de parser le JSON
        donnees = json.loads(contenu)  # json.loads() parse une chaîne JSON
        print(f" {chemin} chargé avec succès")
        return donnees
    
    except FileNotFoundError:
        # Le fichier n'existe pas
        print(f" Fichier introuvable : {chemin}")
        return None
    
    except json.JSONDecodeError as e:
        # Le fichier contient du JSON invalide
        print(f" JSON invalide dans {chemin} : {e.msg} (ligne {e.lineno}, col {e.colno})")
        return None

# Cas 1 : fichier normal qui existe et est valide
data = charger_json_securise("mission_data/missions.json")
if data:
    print(f"   → {len(data['missions'])} missions trouvées")

# Cas 2 : fichier qui n'existe pas
data = charger_json_securise("mission_data/fantome.json")

# Cas 3 : créer un fichier corrompu puis le charger
with open("mission_data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")

data = charger_json_securise("mission_data/corrompu.json")



