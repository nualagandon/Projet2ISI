from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes

def creer_page_accueil(ma_fenetre, connexion) :
    accueil_frame = Frame(ma_fenetre, bg="#f3e0ec")
    accueil_frame.grid(row=1, column=0, sticky="nsew")
    
    #definition de la fonction permettant de savoir quel texte s'affiche en dessous de la barre de progression
    def reste_repas(nb, nb_max) :
        if nb_max == 0 :
            return "Veuillez entrer le nombre de participants dans les paramètres"
        elif nb_max - nb == 0 : 
            return "Il y en a assez."
        else : 
            return "Il en manque " + str(nb_max-nb) + ". "

    Label(accueil_frame, 
          text="Total", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    #choix de la taille des barres de progression
    taille = 400

    ####Partie entrée de la page 
    Label(accueil_frame, 
          text="Entrées", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18)).grid(row=1, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de d'entrées enregistrées dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Entrees;"
    curs.execute(requete)
    nb_entrees = curs.fetchone()[0] or 0
    curs.close()
    #obtenir nombre d'entrées max
    nb_max_entrees = parametres_sauvegardes.get("nb_max_entrees", 1)

    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    ttk.Progressbar(accueil_frame, 
                    length=taille, 
                    value=(nb_entrees / nb_max_entrees * 100) if nb_max_entrees else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=2, column=0, columnspan=2, pady=5)

    Label(accueil_frame, 
          text=reste_repas(nb_entrees, nb_max_entrees), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 8),
          justify="left").grid(row=3, column=0, columnspan=2, pady=5)


    ####Partie plat de la page 
    Label(accueil_frame, 
          text="Plats", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18)).grid(row=4, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de plats enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Plats;"
    curs.execute(requete)
    nb_plats = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de plats max
    nb_max_plats = parametres_sauvegardes.get("nb_max_plats", 1)


    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    ttk.Progressbar(accueil_frame,
                    length=taille, 
                    value=(nb_plats / nb_max_plats * 100) if nb_max_plats else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=5, column=0, columnspan=2, pady=5)

    Label(accueil_frame, 
          text=reste_repas(nb_plats, nb_max_plats), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 8)).grid(row=6, column=0, columnspan=2, pady=5)

    ####Partie desserts de la page 
    Label(accueil_frame,
          text="Desserts", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18)).grid(row=7, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de desserts enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Desserts;"
    curs.execute(requete)
    nb_desserts = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de desserts max
    nb_max_desserts = parametres_sauvegardes.get("nb_max_desserts", 1)



    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    ttk.Progressbar(accueil_frame,
                    length=taille, 
                    value=(nb_desserts / nb_max_desserts * 100) if nb_max_desserts else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=8, column=0, columnspan=2, pady=5)

    Label(accueil_frame, 
          text=reste_repas(nb_desserts, nb_max_desserts), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 8)).grid(row=9, column=0, columnspan=2, pady=5)

    ####Partie desserts de la page 
    Label(accueil_frame, 
          text="Boissons", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18)).grid(row=10, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de boissons enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Boissons;"
    curs.execute(requete)
    nb_boissons = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de boissons max
    nb_max_boissons = parametres_sauvegardes.get("nb_max_boissons", 1)

    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    ttk.Progressbar(accueil_frame, 
                    length=taille, 
                    value=(nb_boissons / nb_max_boissons * 100) if nb_max_boissons else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=11, column=0, columnspan=2, pady=5)

    Label(accueil_frame, 
          text=reste_repas(nb_boissons, nb_max_boissons), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 8)).grid(row=12, column=0, columnspan=2, pady=5)
    

    return accueil_frame