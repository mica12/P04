import sys
from views import vues
from views import vues_menu
from controllers import controleur_joueur
from controllers import controleur_tournoi


class ControleurMenuPrincipal:
    """Controle le menu principal"""

    def __init__(self):
        self.menu_choisi = None
        self.vue = vues.VuePrincipale()
        self.menu_afficher = vues_menu.MenuAfficher()
        self.controleur_menu_joueur = ControleurMenuJoueur()
        self.controleur_menu_tournoi = ControleurMenuTournoi()

    def run(self):
        entree = self.menu_afficher.run(self.menu_afficher.menu_principal)

        if entree == "1":
            print("ok")
            self.menu_choisi = self.controleur_menu_joueur.run()
            return self.menu_choisi

        if entree == "2":
            self.menu_choisi = self.controleur_menu_tournoi.run()
            return self.menu_choisi

        if entree == "q":
            return sys.exit()


class ControleurMenuJoueur:

    def __init__(self):
        self.menu_choisi = None
        self.vue = vues.VueJoueur()
        self.menu_afficher = vues_menu.MenuAfficher()
        self.creer_joueur = controleur_joueur.ControleurCreerJoueur()
        self.creer_rapport_joueur = controleur_joueur.ControleurRapportJoueur()
        self.modifier_classement_joueur = controleur_joueur.ModifierClassementJoueur()

    def run(self):
        print("vous etes dans controleurMenuJoueur")
        entree = self.menu_afficher.run(self.menu_afficher.menu_joueur)

        if entree == "1":
            self.menu_choisi = self.creer_joueur.run()
            print(str(self.menu_choisi))
            return self.menu_choisi

        if entree == "2":
            self.menu_choisi = self.modifier_classement_joueur.run()
            return self.menu_choisi

        if entree == "3":
            self.menu_choisi = self.creer_rapport_joueur.run()
            return self.menu_choisi

        if entree == "4":
            self.menu_choisi = ControleurRetourMenuPrincipal()
            return self.menu_choisi()


class ControleurMenuTournoi:
    def __init__(self):
        self.menu_choisi = None
        self.vue = vues.VuePrincipale()
        self.menu_afficher = vues_menu.MenuAfficher()
        self.controleur_creer_tournoi = controleur_tournoi.ControleurCreerTournoi()
        self.controleur_lancer_tournoi = controleur_tournoi.ControleurLancerTournoi()
        self.controleur_reprendre_tournoi_en_cours = controleur_tournoi.ControleurReprendreTournoi()
        self.creer_rapport_tournoi = controleur_tournoi.RapportTournoi()

    def run(self):
        entree = self.menu_afficher.run(self.menu_afficher.menu_tournoi)

        if entree == "1":
            self.menu_choisi = self.controleur_creer_tournoi.run()
            return self.menu_choisi

        if entree == "2":
            self.menu_choisi = self.controleur_lancer_tournoi.run()
            return self.menu_choisi

        if entree == "3":
            self.menu_choisi = self.controleur_reprendre_tournoi_en_cours.run()
            return self.menu_choisi

        if entree == "4":
            self.menu_choisi = self.creer_rapport_tournoi.run()
            return self.menu_choisi

        if entree == "5":
            self.menu_choisi = ControleurRetourMenuPrincipal()
            return self.menu_choisi()


class ControleurRetourMenuPrincipal:
    def __init__(self):
        self.controleur_menu_principal = ControleurMenuPrincipal()

    def __call__(self):
        self.controleur_menu_principal.run()
