from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes

def creer_page_accueil(ma_fenetre, connexion) :
    accueil_frame = Frame(ma_fenetre, bg="#f3e0ec")
    accueil_frame.grid(row=1, column=0, sticky="nsew")
    accueil_frame.rowconfigure(0, weight=1)
    accueil_frame.columnconfigure(0, weight=1)

    central_frame = Frame(accueil_frame, bg="#f3e0ec")
    central_frame.grid(row=0, column=0, sticky="nsew")
    central_frame.columnconfigure(0, weight=1)  

    for i in range(5):
        central_frame.grid_columnconfigure(i, weight=1)

    # Largeur de la barre de progression  
    taille = 400

    #definition de la fonction permettant de savoir quel texte s'affiche en dessous de la barre de progression
    def reste_repas(nb, nb_max) :
        if nb_max == 0 :
            return "Veuillez entrer le nombre de participants dans les paramètres"
        elif nb_max - nb == 0 : 
            return "Il y en a assez"
        else : 
            return "Il en manque " + str(nb_max-nb)


    Label(central_frame, 
          text="Total", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 28, "bold"),
          anchor="center"
          ).grid(row=0, column=0, columnspan=5, pady=10, sticky="ew")
 
    row = 1

    # --- Entrées ---

    #On récupère le nombre de d'entrées enregistrées dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Entrees;"
    curs.execute(requete)
    nb_entrees = curs.fetchone()[0] or 0
    curs.close()
    #obtenir nombre d'entrées max
    nb_max_entrees = parametres_sauvegardes.get("nb_max_entrees", 1)

    Label(central_frame, 
          text="Entrées", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18),
          anchor="center"
          ).grid(row=row, column=1, columnspan=2, sticky="w", pady=(10, 0))
    row += 1

    progress_frame_entrees = Frame(central_frame, bg="#f3e0ec")
    progress_frame_entrees.grid(row=row, column=1, columnspan=3, pady=(0, 0), sticky="ew")
    progress_frame_entrees.grid_columnconfigure(0, weight=1)

    ttk.Progressbar(progress_frame_entrees, 
                    length=taille, 
                    value=(nb_entrees / nb_max_entrees * 100) if nb_max_entrees else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=0, column=0, sticky="ew")
    row += 1

    Label(central_frame, 
          text=reste_repas(nb_entrees, nb_max_entrees), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 16),
          justify="left"
          ).grid(row=row, column=3, sticky="e", pady=(0, 15))
    row += 1

    # --- Plats ---
    #   
    #On récupère le nombre de plats enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Plats;"
    curs.execute(requete)
    nb_plats = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de plats max
    nb_max_plats = parametres_sauvegardes.get("nb_max_plats", 1)
    
    Label(central_frame, 
          text="Plats", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18),
          anchor="center"
          ).grid(row=row, column=1, columnspan=2, sticky="w", pady=(10, 0))
    row += 1

    # Barre de progression pour les plats
    progress_frame_plats = Frame(central_frame, bg="#f3e0ec")
    progress_frame_plats.grid(row=row, column=1, columnspan=3, pady=(0, 0), sticky="ew")
    progress_frame_plats.grid_columnconfigure(0, weight=1)

    ttk.Progressbar(progress_frame_plats,
                    length=taille, 
                    value=(nb_plats / nb_max_plats * 100) if nb_max_plats else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=0, column=0, sticky="ew")
    row += 1

    Label(central_frame, 
          text=reste_repas(nb_plats, nb_max_plats), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 16)
          ).grid(row=row, column=3, sticky="e", pady=(0, 15))
    row += 1
    
    # --- Desserts ---

    #On récupère le nombre de desserts enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Desserts;"
    curs.execute(requete)
    nb_desserts = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de desserts max
    nb_max_desserts = parametres_sauvegardes.get("nb_max_desserts", 1)

    Label(central_frame,
          text="Desserts", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18),
          anchor="center"
          ).grid(row=row, column=1, columnspan=2, sticky="w", pady=(10, 0))
    row += 1

    # Barre de progression pour les desserts
    progress_frame_desserts = Frame(central_frame, bg="#f3e0ec")
    progress_frame_desserts.grid(row=row, column=1, columnspan=3, pady=(0, 0), sticky="ew")
    progress_frame_desserts.grid_columnconfigure(0, weight=1)

    ttk.Progressbar(progress_frame_desserts,
                    length=taille, 
                    value=(nb_desserts / nb_max_desserts * 100) if nb_max_desserts else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=0, column=0, sticky="ew")
    row += 1

    Label(central_frame, 
          text=reste_repas(nb_desserts, nb_max_desserts), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 16)
          ).grid(row=row, column=3, sticky="e", pady=(0, 15))
    row += 1

    # --- Boissons ---
    
    #On récupère le nombre de boissons enregistré dans la base
    curs = connexion.cursor()
    requete = "select sum(qt_apportee) from Boissons;"
    curs.execute(requete)
    nb_boissons = curs.fetchone()[0] or 0
    curs.close()

    #obtenir nombre de boissons max
    nb_max_boissons = parametres_sauvegardes.get("nb_max_boissons", 1)

    Label(central_frame, 
          text="Boissons", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 18),
          anchor="center"
          ).grid(row=row, column=1, columnspan=2, sticky="w", pady=(10, 0))
    row += 1

    # Barre de progression pour les boissons
    progress_frame_boissons = Frame(central_frame, bg="#f3e0ec")
    progress_frame_boissons.grid(row=row, column=1, columnspan=3, pady=(0, 0), sticky="ew")
    progress_frame_boissons.grid_columnconfigure(0, weight=1)
   
    ttk.Progressbar(progress_frame_boissons, 
                    length=taille, 
                    value=(nb_boissons / nb_max_boissons * 100) if nb_max_boissons else 0,
                    maximum=100,
                    style="pink.Horizontal.TProgressbar"
                    ).grid(row=0, column=0, sticky="ew")
    row += 1

    Label(central_frame, 
          text=reste_repas(nb_boissons, nb_max_boissons), 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 16),
          ).grid(row=row, column=3, sticky="e", pady=(0, 15))
    

    return accueil_frame