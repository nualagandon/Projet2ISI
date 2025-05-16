from tkinter import *
from tkinter import ttk
from database import connecter_bd, creer_tables
from categorie_repas import CategorieRepas
from interface_entrees import creer_page_entrees
from interface_plats import creer_page_plats
from interface_desserts import creer_page_desserts
from interface_boissons import creer_page_boissons
from interface_parametres import creer_page_parametres
from interface_accueil import creer_page_accueil

# Connexion à la base de données
connexion = connecter_bd()
if connexion:
    creer_tables(connexion)
else:
    print("Échec de la connexion à la base de données.")
    exit()


# Création de la fenêtre principale
ma_fenetre = Tk()
ma_fenetre.title("Organisation des repas")

# Personnalisation de la couleur des barres de progression
style = ttk.Style()
style.theme_use("default")
style.configure("pink.Horizontal.TProgressbar", troughcolor="#f3e0ec", background="#450920")

def afficher_page(page):
    """Affiche la page choisie et cache les autres."""
    global parametres_frame
    global accueil_frame
    global entrees_frame
    global plats_frame
    global boissons_frame
    global desserts_frame

    for frame in toutes_les_pages: 
        frame.grid_forget()                    # Ferme toutes les pages
    
    if page == parametres_frame :
        page.grid(row=1, column=0, sticky="nsew")   # Ouvre la page paramètre (est la seule qui n'a pas besoin d'être rafraichie)
    
    else : 
        if page == accueil_frame:
            accueil_frame = creer_page_accueil(ma_fenetre, connexion)
            toutes_les_pages[0] = accueil_frame
            accueil_frame.grid(row=1, column=0, sticky="nsew")  # Ouvre la page d'accueil
        elif page == entrees_frame :
            entrees_frame = creer_page_entrees(ma_fenetre, connexion)
            toutes_les_pages[1] = entrees_frame
            entrees_frame.grid(row=1, column=0, sticky="nsew") # Ouvre la page entrées
        elif page == plats_frame :
            plats_frame = creer_page_plats(ma_fenetre, connexion)
            toutes_les_pages[2] = plats_frame
            plats_frame.grid(row=1, column=0, sticky="nsew") # Ouvre la page plats
        elif page == desserts_frame :
            desserts_frame = creer_page_desserts(ma_fenetre, connexion)
            toutes_les_pages[3] = desserts_frame
            desserts_frame.grid(row=1, column=0, sticky="nsew") # Ouvre la page plats
        elif page == boissons_frame :
            boissons_frame = creer_page_boissons(ma_fenetre, connexion)
            toutes_les_pages[3] = boissons_frame
            boissons_frame.grid(row=1, column=0, sticky="nsew") # Ouvre la page plats
        else:
            page.grid(row=1, column=0, sticky="nsew")   # Ouvre la page parametre

# Création de la page Entrées à l'aide de la fonction creer_page_entrees
entrees_frame = creer_page_entrees(ma_fenetre, connexion)
plats_frame = creer_page_plats(ma_fenetre, connexion)
desserts_frame = creer_page_desserts(ma_fenetre, connexion)
boissons_frame = creer_page_boissons(ma_fenetre, connexion)
accueil_frame = creer_page_accueil(ma_fenetre, connexion)
parametres_frame = creer_page_parametres(ma_fenetre, connexion)

# Liste contenant toutes les pages de l'application
toutes_les_pages = [accueil_frame,entrees_frame, plats_frame,desserts_frame,boissons_frame,parametres_frame]

# Création de la barre de navigation
navbar = Frame(ma_fenetre, bg="#0d1b1e", height=50)
navbar.grid(row=0, column=0, sticky="ew")

# Liste des boutons de la barre de navigation
boutons = [
    ("Accueil", lambda: afficher_page(accueil_frame)),
    ("Entrées", lambda: afficher_page(entrees_frame)),
    ("Plats", lambda: afficher_page(plats_frame)),
    ("Desserts", lambda: afficher_page(desserts_frame)),
    ("Boissons", lambda: afficher_page(boissons_frame)),
    ("Paramètres", lambda: afficher_page(parametres_frame)),
]

# Création des boutons dans barre de navigation
for i, (nom, commande) in enumerate(boutons):
    bouton = Button(
        navbar,
        text=nom,
        command=commande,
        bg="#0d1b1e",
        fg="white",
        font=("Arial", 14)
    )
    bouton.grid(row=0, column=i, padx=8, pady=5)

# Affichage de la page d'entrées par défaut
afficher_page(entrees_frame)

# Boucle principale de l'application
ma_fenetre.mainloop()