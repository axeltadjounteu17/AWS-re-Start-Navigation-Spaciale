import json

# Ouvrir et charger le fichier JSON
# json.load() transforme le contenu JSON en dictionnaire Python
with open("mission_data/missions.json", "r", encoding="utf-8") as f:
    donnees = json.load(f)

# Les missions sont dans la clé "missions" du dictionnaire
missions = donnees["missions"]
print(f"Nombre de missions chargées : {len(missions)}")

# Parcourir la liste des missions et afficher les infos
for mission in missions:
    mid = mission["id"]
    nom = mission["nom"]
    dest = mission["destination"]
    duree = mission["duree_jours"]
    nb_equipage = len(mission["equipage"])  # len() compte les éléments de la liste
    budget = mission["budget_millions_usd"]
    
    # f-string pour formater l'affichage
    # {:,} ajoute des séparateurs de milliers (ex: 18,500)
    print(f"[{mid}] {nom} → {dest} | {duree} jours | Équipage : {nb_equipage} | Budget : {budget:,} M$")

# Additionner tous les budgets
budget_total = 0
for mission in missions:
    budget_total += mission["budget_millions_usd"]

print(f"\n Budget total de toutes les missions : {budget_total:,} M$")

# Trouver la mission la plus longue
# On initialise avec la première mission
plus_longue = missions[0]
plus_courte = missions[0]

for mission in missions:
    if mission["duree_jours"] > plus_longue["duree_jours"]:
        plus_longue = mission
    if mission["duree_jours"] < plus_courte["duree_jours"]:
        plus_courte = mission

print(f" Mission la plus longue : {plus_longue['nom']} ({plus_longue['duree_jours']} jours)")
print(f" Mission la plus courte : {plus_courte['nom']} ({plus_courte['duree_jours']} jours)")

