from models import joueur_model
from views import vues
from views import vues_menu
from operator import attrgetter
from controllers import controleur_principal

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
        self.mois_de_naissance = None
        self.jour_de_naissance = None
        self.annee_de_naissance = None
        self.joueur = joueur_model.Joueur()

    def run(self):

        self.dico_donnees_joueur["nom"] = self.ajouter_nom_joueur()
        self.dico_donnees_joueur["prenom"] = self.ajouter_prenom_joueur()
        self.dico_donnees_joueur["naissance"] = self.ajouter_naissance_joueur()
        self.dico_donnees_joueur["genre"] = self.ajouter_genre_joueur()
        self.dico_donnees_joueur["classement"] = self.ajouter_classement_joueur()
        self.joueur.ajouter_joueur_bdd(self.dico_donnees_joueur)

    def ajouter_nom_joueur(self):
        nom_joueur_valide = False
        while not nom_joueur_valide:
            self.joueur.nom_joueur = input("entrez un nom du joueur : ")
            if len(self.joueur.nom_joueur) > 0:
                nom_joueur_valide = True
            else:
                print("vous devez entrer un nom de joueur valide")
        return self.joueur.nom_joueur

    def ajouter_prenom_joueur(self):
        prenom_joueur_valide = False
        while not prenom_joueur_valide:
            self.joueur.prenom_joueur = input("entrez un prenom du joueur : ")
            if len(self.joueur.prenom_joueur) > 0:
                prenom_joueur_valide = True
            else:
                print("vous devez entrer un nom de joueur valide")
        return self.joueur.prenom_joueur

    def ajouter_naissance_joueur(self):
        jour_naissance_valide = False
        while not jour_naissance_valide:
            self.jour_de_naissance = input("entrez le jour de naissance sur 2 chiffres : ")
            if len(self.jour_de_naissance) == 2 and int(self.jour_de_naissance) <= 31:
                jour_naissance_valide = True
            else:
                print("vous devez entrer un jour valide")

        mois_naissance_valide = False
        while not mois_naissance_valide:
            self.mois_de_naissance = input("entrez le mois de naissance sur 2 chiffres : ")
            if len(self.mois_de_naissance) == 2 and int(self.mois_de_naissance) <= 12:
                mois_naissance_valide = True
            else:
                print("vous devez entrer un mois valide")

        annee_naissance_valide = False
        while not annee_naissance_valide:
            self.annee_de_naissance = input("entrez une année de naissance sur 4 chiffres : ")
            if len(self.annee_de_naissance) == 4 and int(self.annee_de_naissance) <= 2018:
                annee_naissance_valide = True
            else:
                print("vous devez entrer une année valide")

        self.joueur.date_de_naissance_joueur = self.jour_de_naissance + self.mois_de_naissance + self.annee_de_naissance
        return self.joueur.date_de_naissance_joueur

    def ajouter_genre_joueur(self):
        genre_joueur_valide = False
        while not genre_joueur_valide:
            self.joueur.genre_joueur = input("entrez le sexe du joueur H ou F : ")
            if self.joueur.genre_joueur == "H" or self.joueur.genre_joueur == "F":
                genre_joueur_valide = True
            else:
                print("vous devez entrer un genre de joueur valide")
        return self.joueur.genre_joueur

    def ajouter_classement_joueur(self):
        classement_joueur_valide = False
        while not classement_joueur_valide:
            self.joueur.classement_joueur = input("entrez le classement du joueur: ")
            if self.joueur.classement_joueur.isnumeric():
                classement_joueur_valide = True
            else:
                print("vous devez entrer un classement de joueur valide")
        return self.joueur.classement_joueur


class ModifierClassementJoueur:

    def __init__(self):
        self.joueur_bdd = joueur_model.joueur_bdd
        # self.controle_joueur = ControleurCreerJoueur()
        self.list_joueur = vues.VueJoueurs()

    def run(self):
        self.list_joueur.run()
        id_joueur_valide = False
        while not id_joueur_valide:
            id_nouveau_joueur = input("entrez l'identifiant du joueur: ")
            if 0 < int(id_nouveau_joueur) <= len(self.joueur_bdd) and id_nouveau_joueur.isnumeric():
                id_joueur_valide = True
            else:
                print("vous devez entrer un identifiant de joueur valide")

        nouveau_classement_joueur_valide = False
        while not nouveau_classement_joueur_valide:
            nouveau_classement_joueur = input("entrez le nouveau classement du joueur: ")
            if nouveau_classement_joueur.isnumeric():
                nouveau_classement_joueur_valide = True
            else:
                print("vous devez entrer un classement de joueur valide")
        joueur_a_modifier = self.joueur_bdd.get(doc_id=int(id_nouveau_joueur))
        joueur_a_modifier["classement"] = nouveau_classement_joueur
        self.joueur_bdd.update({"classement": int(nouveau_classement_joueur)}, doc_ids=[int(id_nouveau_joueur)])
        self.list_joueur.afficher_un_joueur(joueur_a_modifier)


class ControleurRapportJoueur:

    def __init__(self):
        self.joueur_bdd = joueur_model.joueur_bdd
        self.menu_afficher = vues_menu.MenuAfficher()
        self.joueur = joueur_model.Joueur()
        self.liste_joueur_serialise = []
        self.afficher_rapport_joueur = vues.VueRapportJoueur()

    def run(self):
        controleur_menu_principal = controleur_principal.ControleurRetourMenuPrincipal()
        for joueur in self.joueur_bdd:
            self.liste_joueur_serialise.append(self.joueur.deserialiser(joueur))
        self.afficher_rapport_joueur()

        entree = self.menu_afficher.run(self.menu_afficher.menu_rapport_joueur)

        if entree == "1":
            self.liste_joueur_serialise.sort(key=attrgetter("nom_joueur"))
            self.afficher_rapport_joueur.affichage_alphabetique(self.liste_joueur_serialise)
            input()
            ControleurRapportJoueur.run(self)

        if entree == "2":
            self.liste_joueur_serialise.sort(key=attrgetter("rang_joueur"))
            self.afficher_rapport_joueur.affichage_classement(self.liste_joueur_serialise)
            input()
            ControleurRapportJoueur.run(self)

        if entree == "3":
            return controleur_menu_principal()
