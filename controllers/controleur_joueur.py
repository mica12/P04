from models import joueur_model


class ControleurCreerJoueur:
    """creer un joueur"""

    def __init__(self):
        self.dico_donnees_joueur = {"nom": "",
                                    "prenom": "",
                                    "naissance": "",
                                    "genre": "",
                                    "classement": ""}
        self.dico_nom_joueur = None
        self.dico_prenom_joueur = None
        self.dico_naissance_joueur = None
        self.dico_genre_joueur = None
        self.dico_classement_joueur = None

    def run(self):
        self.dico_donnees_joueur["nom"] = self.ajouter_nom_joueur()
        self.dico_donnees_joueur["prenom"] = self.ajouter_prenom_joueur()
        self.dico_donnees_joueur["naissance"] = self.ajouter_naissance_joueur()
        self.dico_donnees_joueur["genre"] = self.ajouter_genre_joueur()
        self.dico_donnees_joueur["classement"] = self.ajouter_classement_joueur()

        print(self.dico_donnees_joueur)

    def ajouter_nom_joueur(self):
        self.dico_nom_joueur = input("entrez un nom du joueur : ")
        return self.dico_nom_joueur

    def ajouter_prenom_joueur(self):
        self.dico_prenom_joueur = input("entrez un prenom du joueur : ")
        return self.dico_prenom_joueur

    def ajouter_naissance_joueur(self):
        self.dico_naissance_joueur = input("entrez la date de naissance du joueur : ")
        return self.dico_naissance_joueur

    def ajouter_genre_joueur(self):
        self.dico_genre_joueur = input("entrez le genre du joueur : ")
        return self.dico_genre_joueur

    def ajouter_classement_joueur(self):
        self.dico_classement_joueur = input("entrez le classement du joueur : ")
        return self.dico_classement_joueur


class ModifierClassementJoueur:

    def run(self):
        pass


class ControleurRapportJoueur:

    def run(self):
        pass



