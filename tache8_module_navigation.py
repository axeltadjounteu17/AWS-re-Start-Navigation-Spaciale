# Importation du module personnalisé
import navigation
import importlib
importlib.reload(navigation) # Pour s'assurer de prendre les dernières modifs du fichier .py

# 1. Chargement des données des corps célestes
donnees = navigation.charger_corps_celestes()

if donnees:
    # 2. Calcul de distance
    d_terre_mars = navigation.distance_interplanetaire("Terre", "Mars", donnees)
    print(f" -> Distance Terre-Mars : {d_terre_mars:.1f} millions de km")
    
    # 3. Calcul de temps de trajet
    # Si on voyage à 15 km/s
    vitesse = 15.0
    jours = navigation.temps_trajet(d_terre_mars, vitesse)
    print(f" -> Temps estimé à {vitesse} km/s : {jours:.0f} jours (environ {jours/30:.1f} mois)")
    
    # 4. Calcul du poids
    masse_astronaute = 80
    gravite_mars = 3.72
    poids_mars = navigation.poids_sur_corps(masse_astronaute, gravite_mars)
    print(f" -> Un astronaute de {masse_astronaute} kg pèse {poids_mars:.1f} Newtons sur Mars.")
    
    # 5. Delta-V pour Lune
    dv_lune = navigation.delta_v(9.81, 1.62, 100)
    print(f" -> Delta-V pour une mission lunaire (orbite 100km) : {dv_lune:.2f} km/s")



