class Tournoi:
    """creer une instance de tournoi"""
    def __init__(self, nom_tournoi=None,
                 lieu_tournoi=None,
                 date_tournoi=None,
                 nombre_de_tour_tournoi=4,
                 liste_des_tours=None,
                 controle_du_temps=None,
                 identifiants_joueur=None,
                 identifiant_tournoi=None,
                 description_tournoi=None
                 ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_tournoi = date_tournoi
        self.nombre_de_tour_tournoi = nombre_de_tour_tournoi
        self.liste_des_tours = liste_des_tours
        self.controle_du_temps = controle_du_temps
        self.identifiants_joueur = identifiants_joueur
        self.identifiant_tournoi = identifiant_tournoi
        self.description_tournoi = description_tournoi


class Tour:
    """creer une instance de tour"""
    def __init__(self, nom_tour=None,
                 date_debut_tour=None,
                 date_fin_tour=None,
                 liste_de_match_fini=None):
        if liste_de_match_fini is None:
            liste_de_match_fini = []
        self.nom_tour = nom_tour
        self.date_debut_tour = date_debut_tour
        self.date_fin_tour = date_fin_tour
        self.liste_de_match_fini = liste_de_match_fini



