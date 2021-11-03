from models import joueur_model


class VuePrincipale:

    def __call__(self):
        print("********************************")
        print("*APPLICATION GESTION DE TOURNOI*")
        print("********************************")
        print("**********MENU PRINCIPAL********")
        print("********************************")
        print("\n")


class VueTitreJoueur:

    def __call__(self):
        print("********************************")
        print("*APPLICATION GESTION DE TOURNOI*")
        print("********************************")
        print("***********MENU JOUEURS*********")
        print("********************************")
        print("\n")


class VueRapportJoueur:

    def __call__(self):
        print("********************************")
        print("*APPLICATION GESTION DE TOURNOI*")
        print("********************************")
        print("*****MENU RAPPORT JOUEURS*******")
        print("********************************")
        print("\n")

    def affichage_alphabetique(self, liste_joueurs):
        for joueur in liste_joueurs:
            print("nom joueur : " + joueur.nom_joueur + " - prenom joueur : " + joueur.prenom_joueur +
                  " - date de naissance joueur : " + joueur.date_de_naissance_joueur + " - genre du joueur : " +
                  joueur.genre_joueur + " - classement : " + str(joueur.rang_joueur))
        print("\n")
        print("appuyez sur entree pour continuer\n")

    def affichage_classement(self, liste_joueurs):
        for joueur in liste_joueurs:
            print("classement : " + str(joueur.rang_joueur) + " - nom joueur : " + joueur.nom_joueur +
                  " - prenom joueur : " + joueur.prenom_joueur + " - date de naissance joueur : "
                  + joueur.date_de_naissance_joueur + " - genre du joueur : " + joueur.genre_joueur)
        print("\n")
        print("appuyez sur entree pour continuer \n")


class VueJoueurs:
    def __init__(self):
        self.joueur_bdd = joueur_model.joueur_bdd

    def run(self):
        print("voici la liste des joueurs")
        for joueur in self.joueur_bdd:
            print("identifiant joueur: " + str(joueur["id"]) + " - Nom joueur: " + joueur["nom"] +
                  " - Prenom: " + joueur["prenom"] + " - Date de naissance : " + joueur["naissance"]
                  + " - Genre du joueur: " + joueur["genre"] + " - Classement: " + str(joueur["classement"])
                  + " - Score: " + str(joueur["score"])
                  )

    def afficher_un_joueur(self, joueur_a_modifier):
        print("informations du joueur mise à jour:")
        print("identifiant joueur: " + str(joueur_a_modifier["id"]) + " - Nom joueur: " + joueur_a_modifier["nom"] +
              " - Prenom: " + joueur_a_modifier["prenom"] + " - Nouveau Classement: "
              + str(joueur_a_modifier["classement"])
              )
