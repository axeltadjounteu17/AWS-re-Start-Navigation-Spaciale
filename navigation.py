# --- navigation.py ---
"""
Module de calculs pour la navigation spatiale.
Ce module contient des fonctions pour estimer les distances, les temps de trajet
et les besoins énergétiques entre les corps célestes.
"""

import json
import math

def distance_interplanetaire(nom_corps1, nom_corps2, donnees_corps):
    """
    Calcule la distance approximative entre deux corps célestes
    basée sur leur distance au Soleil (en millions de km).
    """
    d1 = 0
    d2 = 0
    
    for c in donnees_corps['corps_celestes']:
        if c['nom'] == nom_corps1:
            d1 = c['distance_soleil_mkm']
        if c['nom'] == nom_corps2:
            d2 = c['distance_soleil_mkm']
            
    return abs(d1 - d2)

def temps_trajet(distance_mkm, vitesse_km_s):
    """
    Calcule le temps de trajet en jours.
    distance en millions de km, vitesse en km/s.
    """
    if vitesse_km_s <= 0:
        return float('inf')
        
    # Convertir distance en km : distance_mkm * 1 000 000
    distance_km = distance_mkm * 1_000_000
    
    # Temps en secondes
    temps_secondes = distance_km / vitesse_km_s
    
    # Convertir en jours (1 jour = 24 * 3600 secondes)
    temps_jours = temps_secondes / (24 * 3600)
    
    return temps_jours

def delta_v(gravite_depart, gravite_arrivee, altitude_orbite_km):
    """
    Estimation simplifiée du delta-v nécessaire (en km/s).
    Formule simplifiée : sqrt(2 * g_depart * alt) + sqrt(2 * g_arrivee * alt)
    """
    # Conversion altitude en mètres
    alt_m = altitude_orbite_km * 1000
    
    # Calcul simplifié
    dv = (math.sqrt(2 * gravite_depart * alt_m) + math.sqrt(2 * gravite_arrivee * alt_m)) / 1000
    
    return dv

def poids_sur_corps(masse_kg, gravite_m_s2):
    """Calcule le poids (en Newtons) sur un corps céleste (P = m * g)."""
    return masse_kg * gravite_m_s2

def charger_corps_celestes(chemin="mission_data/corps_celestes.json"):
    """Charge le fichier des corps célestes avec gestion d'erreur."""
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement des corps célestes : {e}")
        return None

if __name__ == "__main__":
    # Tests unitaires du module
    print("--- Tests du module navigation.py ---")
    corps = charger_corps_celestes()
    
    if corps:
        d = distance_interplanetaire("Terre", "Mars", corps)
        print(f"Distance Terre-Mars : {d:.1f} millions km")
        
        t = temps_trajet(d, 11.0)
        print(f"Temps de trajet à 11 km/s : {t:.0f} jours")
        
        dv = delta_v(9.81, 3.72, 400)
        print(f"Delta-V estimé pour orbite 400km : {dv:.2f} km/s")
        
        poids = poids_sur_corps(80, 3.72)
        print(f"Poids d'un astronaute (80 kg) sur Mars : {poids:.1f} N")
