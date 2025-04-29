from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas

def creer_page_accueil(ma_fenetre, connexion) :
    accueil_frame = Frame(ma_fenetre, bg="#f3e0ec")
    accueil_frame.grid(row=1, column=0, sticky="nsew")

    

    Label(accueil_frame, text="Total", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    #choix de la taille des barres de progression
    taille = 400

    ####Partie entrée de la page 
    entree_accueil_frame = Frame(accueil_frame)
    Label(entree_accueil_frame, text="Entrées", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=5)
    
    #On récupère le nombre de plats enregistré dans la base
    curs = connexion.cursor()
    requete = f"count(*) from Entrees;"
    nb = curs.execute(requete)
    curs.close()
    #nommer dans interface parametre, le maximum du nombre d'entree dans chaque etape du repas est nb_max_etape
    barre_entree = ttk.Progressbar(entree_accueil_frame, length=taille).pack(pady=(taille - ((nb_max_entrees - nb)/100 * taille)))
    
    






    return accueil_frame