from tinydb import TinyDB


joueur_bdd = TinyDB('models/joueurs.json')

class Joueur:
    """creer une instance de joueur"""
    def __init__(self, nom_joueur=None,
                 prenom_joueur=None,
                 date_de_naissance_joueur=None,
                 genre_joueur=None,
                 rang_joueur=0,
                 score_tournoi_joueur=0,
                 id_joueur=0,
                 nouveau_classement_joueur = 0
                 ):
        self.nom_joueur = nom_joueur
        self.prenom_joueur = prenom_joueur
        self.date_de_naissance_joueur = date_de_naissance_joueur
        self.genre_joueur = genre_joueur
        self.rang_joueur = rang_joueur
        self.score_tournoi_joueur = score_tournoi_joueur
        self.id_joueur = id_joueur


    def serialiser(self):
        dico_donnees_joueur = {}
        dico_donnees_joueur["nom"] = self.nom_joueur
        dico_donnees_joueur["prenom"] = self.prenom_joueur
        dico_donnees_joueur["naissance"] = self.date_de_naissance_joueur
        dico_donnees_joueur["genre"] = self.genre_joueur
        dico_donnees_joueur["classement"] = int(self.rang_joueur)
        dico_donnees_joueur["score"] = self.score_tournoi_joueur
        dico_donnees_joueur["id"] = self.id_joueur
        return dico_donnees_joueur

    def ajouter_joueur_bdd(self, dico_donnees_joueur):
        self.joueur = Joueur(dico_donnees_joueur["nom"],
                             dico_donnees_joueur["prenom"],
                             dico_donnees_joueur["naissance"],
                             dico_donnees_joueur["genre"],
                             dico_donnees_joueur["classement"]
                             )
        id_joueur = joueur_bdd.insert(self.joueur.serialiser())
        joueur_bdd.update({"id": id_joueur}, doc_ids=[id_joueur])

    def deserialiser(self, joueur_serialise):
        nom_joueur = joueur_serialise["nom"]
        prenom_joueur = joueur_serialise["prenom"]
        date_de_naissance_joueur = joueur_serialise["naissance"]
        genre_joueur = joueur_serialise["genre"]
        rang_joueur = joueur_serialise["classement"]
        score_tournoi_joueur = joueur_serialise["score"]
        id_joueur = joueur_serialise["id"]
        return Joueur(nom_joueur, prenom_joueur, date_de_naissance_joueur, genre_joueur, rang_joueur,
                      score_tournoi_joueur, id_joueur)













        
