class MenuAfficher:
    """affiche les menus"""

    def __init__(self):
        self.menu = None
        self.clef = None
        self.valeur = None

    menu_principal = {"1": "Menu Joueur",
                      "2": "Menu Tournoi",
                      "q": "Quitter"
                      }

    menu_joueur = {"1": "ajouter joueur",
                   "2": "mise a jour classement joueur",
                   "3": "menu rapport joueur",
                   "4": "menu principal"
                   }

    menu_tournoi = {"1": "creer un tournoi",
                    "2": "lancer tournoi",
                    "3": "reprise partie",
                    "4": "menu rapport tournoi",
                    "5": "menu principal"
                    }

    menu_temps = {"1": "bullet",
                  "2": "blitz",
                  "3": "coup rapide"
                  }

    menu_rapport_joueur = {"1": "liste alphabetique joueurs",
                           "2": "liste joueurs classés",
                           "3": "retour menu principal"
                           }

    menu_rapport_tournoi = {"1": "liste des tournois",
                            "2": "selectionner tournoi",
                            "3": "retour au menu principal"
                            }

    def run(self, menu):
        self.menu = menu
        for clef, valeur in self.menu.items():
            print(clef + ":" + valeur)
        while True:
            choix = input(">>")
            for clef in self.menu.items():
                if choix == clef[0]:
                    return choix

            print("vous n'avez pas entré la bonne valeur")
