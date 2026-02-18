# On ouvre le fichier en mode lecture avec l'encodage UTF-8
# Le mot-clé 'with' ferme automatiquement le fichier après utilisation
with open("mission_data/journal_bord.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()  # readlines() retourne une liste de lignes

# Afficher le nombre total de lignes
print(f"Journal de bord : {len(lignes)} entrées")

# On cherche les lignes qui contiennent le mot "alerte" (en minuscule ou majuscule)
# .lower() convertit la ligne en minuscules pour comparer facilement
alertes = []
for ligne in lignes:
    if "alerte" in ligne.lower():
        alertes.append(ligne)

# Afficher les alertes trouvées
print(f"--- Alertes détectées ({len(alertes)}) ---")
for alerte in alertes:
    print(alerte.strip())  # strip() enlève les espaces et sauts de ligne en trop

# On ouvre un nouveau fichier en mode écriture ("w" = write)
# Si le fichier n'existe pas, il sera créé automatiquement
with open("mission_data/alertes.txt", "w", encoding="utf-8") as fichier_alertes:
    for alerte in alertes:
        fichier_alertes.write(alerte)

print(" Fichier alertes.txt créé.")

