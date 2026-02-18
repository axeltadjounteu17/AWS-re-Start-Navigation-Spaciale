# --- exceptions.py ---
"""
Module contenant les exceptions personnalisées pour la navigation spatiale.
"""

class NavigationError(Exception):
    """Classe de base pour toutes les erreurs liées à la navigation spatiale."""
    pass

class MissionDataError(NavigationError):
    """Erreur levée lorsque les données d'une mission sont invalides ou incomplètes."""
    pass

class TrajectoireError(NavigationError):
    """Erreur levée lorsque les paramètres de trajectoire (distance/durée) sont incohérents."""
    pass

class CarburantError(NavigationError):
    """Erreur levée lorsque le niveau de carburant est critique."""
    pass
