from models import joueur_model
from models import tournoi_model
from views import vues
from views import vues_menu
from operator import attrgetter
from controllers import controleur_principal


class ControleurCreerTournoi:
    def __init__(self):
        self.dico_donnees_tournoi = {"nom tournoi": "",
                                     "lieu tournoi": "",
                                     "date tournoi": "",
                                     "nombre de tour tournoi": "",
                                     "controle du temps": "",
                                     "description du tournoi": ""}

        self.tournoi = tournoi_model.Tournoi()
        self.menu_afficher = vues_menu.MenuAfficher()
        self.list_joueur = vues.VueJoueurs()
        self.joueur_ids = []

    def run(self):
        self.dico_donnees_tournoi["nom tournoi"] = self.ajouter_nom_tournoi()
        self.dico_donnees_tournoi["lieu tournoi"] = self.ajouter_lieu_tournoi()
        self.dico_donnees_tournoi["date tournoi"] = self.ajouter_date_tournoi()
        self.dico_donnees_tournoi["nombre de tour tournoi"] = 4
        self.dico_donnees_tournoi["controle du temps"] = self.ajouter_controle_du_temps()
        self.dico_donnees_tournoi["description du tournoi"] = self.ajouter_description_tournoi()
        self.ajouter_joueur_tournoi()
        self.tournoi.ajouter_tournoi_bdd(self.dico_donnees_tournoi)
        controleur_menu_principal = controleur_principal.ControleurRetourMenuPrincipal()
        controleur_menu_principal()

    def ajouter_nom_tournoi(self):
        nom_tournoi_valide = False
        while not nom_tournoi_valide:
            self.tournoi.nom_tournoi = input("entrez un nom du tournoi: ")
            if len(self.tournoi.nom_tournoi) > 0:
                nom_tournoi_valide = True
            else:
                print("vous devez entrer un nom de tournoi valide")
        return self.tournoi.nom_tournoi

    def ajouter_lieu_tournoi(self):
        lieu_tournoi_valide = False
        while not lieu_tournoi_valide:
            self.tournoi.lieu_tournoi = input("entrez un lieu : ")
            if len(self.tournoi.nom_tournoi) > 0:
                lieu_tournoi_valide = True
            else:
                print("vous devez entrer un lieu valide")
        return self.tournoi.lieu_tournoi

    def ajouter_date_tournoi(self):
        jour_tournoi_valide = False
        while not jour_tournoi_valide:
            self.jour_tournoi= input("entrez le jour sur 2 chiffres : ")
            if len(self.jour_tournoi) == 2 and int(self.jour_tournoi) <= 31:
                jour_tournoi_valide = True
            else:
                print("vous devez entrer un jour valide")

        mois_tournoi_valide = False
        while not mois_tournoi_valide:
            self.mois_tournoi = input("entrez le mois sur 2 chiffres : ")
            if len(self.mois_tournoi) == 2 and int(self.mois_tournoi) <= 12:
                mois_tournoi_valide = True
            else:
                print("vous devez entrer un mois valide")

        annee_tournoi_valide = False
        while not annee_tournoi_valide:
            self.annee_tournoi = input("entrez une année sur 4 chiffres : ")
            if len(self.annee_tournoi) == 4 and int(self.annee_tournoi) <= 2021:
                annee_tournoi_valide = True
            else:
                print("vous devez entrer une année valide")

        self.tournoi.date_tournoi = self.jour_tournoi + self.mois_tournoi + self.annee_tournoi
        return self.tournoi.date_tournoi

    def ajouter_controle_du_temps(self):
        print("Choisir le controle du temps :")
        entree = self.menu_afficher.run(self.menu_afficher.menu_temps)
        if entree == "1":
            self.tournoi.controle_du_temps = "bullet"
        if entree == "2":
            self.tournoi.controle_du_temps = "blitz"
        if entree == "3":
            self.tournoi.controle_du_temps = "coup rapide"
        return self.tournoi.controle_du_temps

    def ajouter_description_tournoi(self):
        description_tournoi_valide = False
        while not description_tournoi_valide:
            self.tournoi.description_tournoi = input("entrez une description du tournoi: ")
            if len(self.tournoi.description_tournoi) > 0:
                description_tournoi_valide = True
            else:
                print("vous devez entrer une description valide")
        return self.tournoi.description_tournoi

    def ajouter_joueur_tournoi(self):
        controleur_menu_principal = controleur_principal.ControleurRetourMenuPrincipal()
        choisir_joueur_valide = None
        while not choisir_joueur_valide :
            choisir_joueur = input("souhaitez vous ajouter un joueur : ")
            if choisir_joueur == "oui":
                choisir_joueur_valide = True
            elif choisir_joueur == "non":
                choisir_joueur_valide = True
                controleur_menu_principal()
            else:
                print("vous devez choisir oui ou non")
        self.list_joueur.run()
        choix_joueur_id_valide = False
        while not choix_joueur_id_valide:
            choix_joueur_id = input("choisir un identifiant de joueur dans la liste : ")
            if int(choix_joueur_id) <= 0 or int(choix_joueur_id) > len(joueur_model.joueur_bdd):
                print("vous devez choisir un joueur dans la liste")
            elif choix_joueur_id in self.joueur_ids:
                print("vous avez deja choisi ce joueur")
            else:
                choix_joueur_id_valide = True

        self.joueur_ids.append(choix_joueur_id)
        print("liste des joueur du tournoi" + str(self.joueur_ids))
        self.ajouter_joueur_tournoi()

        for id_joueur in self.joueur_ids:
            joueur = joueur_model.joueur_bdd.get(doc_id=id_joueur)
            self.joueur_serialise.append(joueur)


class ControleurLancerTournoi:
    def run(self):
        pass


class ControleurReprendreTournoi:
    def run(self):
        pass

class RapportTournoi:
    def run(self):
        pass


