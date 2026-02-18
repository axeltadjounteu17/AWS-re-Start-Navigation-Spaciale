# --- centre_controle.py ---
"""
🚀 CENTRE DE CONTRÔLE DE MISSION SPATIALE 🚀
Programme principal intégrant toutes les fonctionnalités du projet.
"""

import os
import json
import datetime
import navigation
from exceptions import NavigationError, MissionDataError

# Configuration des chemins
DATA_DIR = "mission_data"
MISSIONS_FILE = os.path.join(DATA_DIR, "missions.json")
TELEMETRIE_FILE = os.path.join(DATA_DIR, "telemetrie.json")
CORPS_FILE = os.path.join(DATA_DIR, "corps_celestes.json")
JOURNAL_FILE = os.path.join(DATA_DIR, "journal_bord.txt")
LOG_FILE = os.path.join(DATA_DIR, "rapports", "log_controle.txt")

def logger(message):
    """Enregistre une action dans le fichier log."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    horodateur = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{horodateur}] {message}\n")

def afficher_menu():
    print("\n" + "═"*50)
    print("🚀 CENTRE DE CONTRÔLE DE MISSION 🚀".center(50))
    print("═"*50)
    print("  1. Afficher toutes les missions")
    print("  2. Détails d'une mission (par ID)")
    print("  3. Ajouter une nouvelle mission")
    print("  4. Télémétrie en temps réel (dernier relevé)")
    print("  5. Calculateur de navigation")
    print("  6. Diagnostic système (alertes)")
    print("  7. Recherche dans le journal de bord")
    print("  8. Générer un rapport complet")
    print("  9. Arborescence des fichiers mission")
    print("  0. Quitter")
    print("═"*50)

def option_1_afficher_missions():
    logger("Consultation de la liste des missions.")
    try:
        with open(MISSIONS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("\n--- LISTE DES MISSIONS ---")
        for m in data['missions']:
            print(f"[{m['id']}] {m['nom']} → {m['destination']}")
    except Exception as e:
        print(f"Erreur : {e}")

def option_2_details_mission():
    mission_id = input("Entrez l'ID de la mission (ex: MSN-002) : ").upper()
    logger(f"Consultation détails mission {mission_id}.")
    try:
        with open(MISSIONS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        mission = next((m for m in data['missions'] if m['id'] == mission_id), None)
        
        if mission:
            print(f"\n--- DÉTAILS {mission['id']} ({mission['nom']}) ---")
            print(f"Destination : {mission['destination']}")
            print(f"Statut      : {mission['statut']}")
            print(f"Équipage    : {', '.join(mission['equipage']) if mission['equipage'] else 'Sonde non habitée'}")
            print(f"Budget      : {mission['budget_millions_usd']} M$")
            
            # Utilisation de navigation.py pour le poids
            corps_data = navigation.charger_corps_celestes(CORPS_FILE)
            for c in corps_data['corps_celestes']:
                if c['nom'] == mission['destination']:
                    poids = navigation.poids_sur_corps(80, c['gravite_m_s2'])
                    print(f"Poids d'un astronaute (80kg) là-bas : {poids:.1f} N")
        else:
            print("Mission introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")

def option_3_ajouter_mission():
    print("\n--- AJOUTER UNE MISSION ---")
    try:
        id_m = input("ID (ex MSN-007) : ").upper()
        nom = input("Nom : ")
        dest = input("Destination : ")
        date = input("Date (AAAA-MM-JJ) : ")
        duree = int(input("Durée (jours) : "))
        budget = int(input("Budget (M$) : "))
        
        nouvelle = {
            "id": id_m, "nom": nom, "destination": dest,
            "date_lancement": date, "statut": "planifiée",
            "equipage": [], "duree_jours": duree, "budget_millions_usd": budget
        }
        
        with open(MISSIONS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if any(m['id'] == id_m for m in data['missions']):
            print("❌ Erreur : Cet ID existe déjà.")
            return

        data['missions'].append(nouvelle)
        with open(MISSIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Mission '{nom}' ajoutée avec succès !")
        logger(f"Ajout mission {id_m}.")
    except Exception as e:
        print(f"❌ Erreur lors de l'ajout : {e}")

def option_4_telemetrie():
    logger("Consultation de la télémétrie.")
    try:
        with open(TELEMETRIE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        dernier = data['releves'][-1]
        
        print(f"\n--- STATUT ACTUEL ({data['vaisseau']}) ---")
        print(f"Phase    : {dernier['phase']}")
        print(f"Altitude : {dernier['altitude_km']:,} km")
        
        pct = dernier['carburant_pct']
        if pct > 50: status = "🟢 OK"
        elif pct > 20: status = "🟡 BAS"
        else: status = "🔴 CRITIQUE"
        print(f"Carburant: {pct}% {status}")
        
        sys_status = [s for s, v in dernier['systemes'].items() if v != "nominal"]
        print(f"Alertes  : {', '.join(sys_status) if sys_status else 'Aucune'}")
    except Exception as e:
        print(f"Erreur : {e}")

def option_5_calculateur():
    print("\n--- CALCULATEUR DE TRAJET ---")
    depart = input("Départ (ex: Terre) : ")
    arrivee = input("Arrivée (ex: Mars) : ")
    logger(f"Calcul trajet {depart} -> {arrivee}.")
    
    corps = navigation.charger_corps_celestes(CORPS_FILE)
    if not corps: return
    
    dist = navigation.distance_interplanetaire(depart, arrivee, corps)
    temps = navigation.temps_trajet(dist, 11.0)
    
    print(f"📍 Distance estimée : {dist:.1f} millions de km")
    print(f"⏱️ Temps de trajet (à 11 km/s) : {temps:.0f} jours")

def option_6_diagnostic():
    print("\n--- DIAGNOSTIC SYSTÈME (ALERTE) ---")
    logger("Exécution diagnostic système.")
    try:
        with open(TELEMETRIE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        anomalies = 0
        for r in data['releves']:
            alertes = [s for s, v in r['systemes'].items() if v != "nominal"]
            if alertes:
                print(f"⚠️ [{r['timestamp']}] Anomalies : {', '.join(alertes)}")
                anomalies += 1
        
        if anomalies == 0:
            print("✅ Aucun problème détecté dans l'historique.")
        else:
            print(f"\nTotal : {anomalies} relevés avec alertes.")
    except Exception as e:
        print(f"Erreur : {e}")

def option_7_recherche_journal():
    print("\n--- RECHERCHE DANS LE JOURNAL ---")
    mot = input("Mot-clé à rechercher : ").lower()
    logger(f"Recherche '{mot}' dans le journal.")
    try:
        trouve = False
        with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if mot in line.lower():
                    print(f"📖 {line.strip()}")
                    trouve = True
        if not trouve: 
            print("Aucune entrée correspondante.")
    except Exception as e:
        print(f"Erreur : {e}")

def option_8_rapport_complet():
    print("\nGénération du rapport complet...")
    logger("Génération rapport complet.")
    try:
        with open(MISSIONS_FILE, 'r', encoding='utf-8') as f: missions = json.load(f)
        with open(TELEMETRIE_FILE, 'r', encoding='utf-8') as f: tele = json.load(f)
        
        rapport = {
            "genere_le": str(datetime.datetime.now()),
            "total_missions": len(missions['missions']),
            "vaisseau": tele['vaisseau'],
            "dernier_releve": tele['releves'][-1]
        }
        
        dest_path = os.path.join(DATA_DIR, "rapports", "rapport_complet.json")
        with open(dest_path, 'w', encoding='utf-8') as f:
            json.dump(rapport, f, indent=2, ensure_ascii=False)
        print(f"✅ Rapport complet sauvegardé dans : {dest_path}")
    except Exception as e:
        print(f"Erreur : {e}")

def option_9_arborescence():
    logger("Affichage de l'arborescence.")
    print(f"\nStructure de {DATA_DIR} :")
    for root, dirs, files in os.walk(DATA_DIR):
        level = root.replace(DATA_DIR, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}📄 {f}")

def main():
    while True:
        try:
            afficher_menu()
            choix = input("Votre choix : ")
            
            if choix == "1": option_1_afficher_missions()
            elif choix == "2": option_2_details_mission()
            elif choix == "3": option_3_ajouter_mission()
            elif choix == "4": option_4_telemetrie()
            elif choix == "5": option_5_calculateur()
            elif choix == "6": option_6_diagnostic()
            elif choix == "7": option_7_recherche_journal()
            elif choix == "8": option_8_rapport_complet()
            elif choix == "9": option_9_arborescence()
            elif choix == "0":
                print(" Fermeture du centre de contrôle. Au revoir !")
                logger("Session terminée.")
                break
            else:
                print("❌ Option invalide. Réessayez.")
        except KeyboardInterrupt:
            print("\nArrêt forcé.")
            break
        except Exception as e:
            print(f"⚠️ Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()
