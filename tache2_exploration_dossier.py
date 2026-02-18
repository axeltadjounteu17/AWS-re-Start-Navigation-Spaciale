import os

# Nom du dossier à explorer
dossier = "mission_data"

# Vérifier si le dossier existe
if os.path.exists(dossier):
    print(f"Le dossier '{dossier}' existe.")
else:
    print(f" Erreur : le dossier '{dossier}' n'existe pas !")

# os.listdir() retourne la liste des éléments dans le dossier
print(f" {dossier}/")

for element in os.listdir(dossier):
    chemin_complet = os.path.join(dossier, element)  # Construire le chemin complet
    
    if os.path.isfile(chemin_complet):
        # os.path.getsize() retourne la taille en octets
        taille_octets = os.path.getsize(chemin_complet)
        taille_ko = taille_octets / 1024  # Convertir en Ko
        print(f"    {element:<25} ({taille_ko:.1f} Ko)")
    elif os.path.isdir(chemin_complet):
        print(f"    {element}/")

# Créer le sous-dossier rapports/ s'il n'existe pas
chemin_rapports = os.path.join(dossier, "rapports")
if not os.path.exists(chemin_rapports):
    os.makedirs(chemin_rapports)
    print(f"    rapports/               [créé]")
else:
    print(f"    rapports/               [existe déjà]")

# Créer le sous-dossier archives/ s'il n'existe pas
chemin_archives = os.path.join(dossier, "archives")
if not os.path.exists(chemin_archives):
    os.makedirs(chemin_archives)
    print(f"    archives/               [créé]")
else:
    print(f"    archives/               [existe déjà]")

# Afficher l'arborescence complète du dossier
print(f"\n {dossier}/")
for element in sorted(os.listdir(dossier)):
    chemin_complet = os.path.join(dossier, element)
    
    if os.path.isfile(chemin_complet):
        taille_ko = os.path.getsize(chemin_complet) / 1024
        print(f"    {element:<25} ({taille_ko:.1f} Ko)")
    elif os.path.isdir(chemin_complet):
        print(f"    {element}/")
        # Lister aussi le contenu des sous-dossiers
        for sous_element in os.listdir(chemin_complet):
            print(f"      └── {sous_element}")

