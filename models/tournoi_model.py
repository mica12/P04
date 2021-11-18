from tinydb import TinyDB

tournoi_bdd = TinyDB('models/tournoi.json')

class Tournoi:
    """creer une instance de tournoi"""

    def __init__(self, nom_tournoi=None,
                 lieu_tournoi=None,
                 date_tournoi=None,
                 nombre_de_tour_tournoi=4,
                 liste_des_tours=None,
                 controle_du_temps=None,
                 identifiants_joueurs_tournoi=None,
                 identifiant_tournoi=None,
                 description_tournoi=None
                 ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_tournoi = date_tournoi
        self.nombre_de_tour_tournoi = nombre_de_tour_tournoi
        self.liste_des_tours = liste_des_tours
        self.controle_du_temps = controle_du_temps
        self.identifiants_joueur = identifiants_joueurs_tournoi
        self.identifiant_tournoi = identifiant_tournoi
        self.description_tournoi = description_tournoi

    def serialiser_tournoi(self):
        dico_donnees_tournoi = {}
        dico_donnees_tournoi["nom tournoi"] = self.nom_tournoi
        dico_donnees_tournoi["lieu tournoi"] = self.lieu_tournoi
        dico_donnees_tournoi["date tournoi"] = self.date_tournoi
        dico_donnees_tournoi["nombre de tour tournoi"] = self.nombre_de_tour_tournoi
        dico_donnees_tournoi["liste de tour tournoi"] = self.liste_des_tours
        dico_donnees_tournoi["controle du temps"] = self.controle_du_temps
        #dico_donnees_tournoi["identifiants des joueurs du tournoi"] = self.identifiants_joueurs_tournoi
        #dico_donnees_tournoi["identifiant du tournoi"] = self.identifiant_tournoi
        #dico_donnees_tournoi["description du tournoi"] = self.description_tournoi
        return dico_donnees_tournoi

    def deserialiser_tournoi(self, tournoi_serialise):
        nom_tournoi = tournoi_serialise["nom tournoi"]
        lieu_tournoi = tournoi_serialise["lieu tournoi"]
        date_tournoi = tournoi_serialise["date tournoi"]
        nombre_de_tour_tournoi = tournoi_serialise["nombre de tour tournoi"]
        liste_des_tours = tournoi_serialise["liste de tour tournoi"]
        controle_du_temps = tournoi_serialise["controle du temps"]
        identifiants_joueurs_tournoi = tournoi_serialise["identifiants des joueurs du tournoi"]
        identifiant_tournoi = tournoi_serialise["identifiant du tournoi"]
        description_tournoi = tournoi_serialise["description du tournoi"]
        return Tournoi(nom_tournoi, lieu_tournoi, date_tournoi, nombre_de_tour_tournoi, liste_des_tours,
                       controle_du_temps, identifiants_joueurs_tournoi, identifiant_tournoi, description_tournoi)

    def ajouter_tournoi_bdd(self, dico_donnees_tournoi):
        self.tournoi = Tournoi(dico_donnees_tournoi["nom tournoi"],
                               dico_donnees_tournoi["lieu tournoi"],
                               dico_donnees_tournoi["date tournoi"],
                               dico_donnees_tournoi["nombre de tour tournoi"],
                               dico_donnees_tournoi["controle du temps"],
                               dico_donnees_tournoi["description du tournoi"]
                               #dico_donnees_tournoi["identifiants des joueurs du tournoi"]
                               )
        identifiant_tournoi = tournoi_bdd.insert(self.tournoi.serialiser_tournoi())
        tournoi_bdd.update({"id": identifiant_tournoi}, doc_ids=[identifiant_tournoi])


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
