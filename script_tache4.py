# --- script_tache4_exceptions.py ---
"""
OBJECTIF : Gérer les erreurs de lecture de fichiers (Robustesse).
"""

import json

def charger_json_securise(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Erreur : Fichier '{chemin}' introuvable.")
    except json.JSONDecodeError:
        print(f"❌ Erreur : Le fichier '{chemin}' contient du texte mal formé.")
    except Exception as e:
        print(f"❌ Une erreur inconnue est survenue : {e}")
    return None

# Test
print("Test 1 (Normal) :")
data = charger_json_securise("mission_data/missions.json")
if data: print("✅ Chargement réussi.")

print("\nTest 2 (Fichier inexistant) :")
charger_json_securise("inexistant.json")
