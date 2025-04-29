from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas

def creer_page_accueil(ma_fenetre, connexion) :
    accueil_frame = Frame(ma_fenetre, bg="#f3e0ec")
    accueil_frame.grid(row=1, column=0, sticky="nsew")

    #definition de la fonction permettant de savoir quel texte s'affiche en dessous de la barre de progression
    def reste_repas(nb, nb_max) :
        if nb_max - nb == 0 : 
            return "Il y en a assez."
        else : 
            return "Il en manque " + (nb_max-nb) + ". "
    

    Label(accueil_frame, text="Total", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    #choix de la taille des barres de progression
    taille = 400

    ####Partie entrée de la page 
    entree_accueil_frame = Frame(accueil_frame)
    Label(entree_accueil_frame, text="Entrées", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de plats enregistré dans la base
    curs = connexion.cursor()
    requete = "count(*) from Entrees;"
    nb_entrees = curs.execute(requete)
    curs.close()
    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    barre_entree = ttk.Progressbar(entree_accueil_frame, length=taille).pack(pady=(taille - ((nb_max_entrees - nb_entrees)/100 * taille)))
    barre_entree.place(x=30, y = 30)

    Label(entree_accueil_frame, text=reste_repas(nb_entrees, nb_max_entrees), bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=3, column=0, columnspan=2, pady=5)






    return accueil_frame