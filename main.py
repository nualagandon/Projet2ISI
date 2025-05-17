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
style.configure("pink.Horizontal.TProgressbar", troughcolor="white", background="#a53860", bordercolor="#a53860")

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
toutes_les_pages = [None, entrees_frame, plats_frame, desserts_frame, boissons_frame, parametres_frame]

ma_fenetre.rowconfigure(1, weight=1)
ma_fenetre.columnconfigure(0, weight=1)

# Création de la barre de navigation

# Ajout d'un frame pour gérer l'alignement de la barre de navigation
navbar_frame = Frame(ma_fenetre, bg="#0d1b1e")
navbar_frame.grid(row=0, column=0, sticky="ew")
navbar_frame.grid_columnconfigure(0, weight=1)
navbar_frame.grid_columnconfigure(1, weight=0)

navbar = Frame(navbar_frame, bg="#0d1b1e", height=50)
navbar.grid(row=0, column=0, sticky="e")

# Suivi des boutons de la barre de navigation
boutons_widgets = []

def afficher_page_et_surbrillance(index):
    global accueil_frame


    print(f"Affichage de la page index {index}")


    # Masquer toutes les pages
    for frame in toutes_les_pages:
        if frame is not None:
            frame.grid_forget()

    # Si la page est l'accueil (index 0), on la crée à nouveau afin de mettre à jour les données pour les barres de progression
    if index == 0:
        accueil_frame = creer_page_accueil(ma_fenetre, connexion)
        toutes_les_pages[0] = accueil_frame
        accueil_frame.grid(row=1, column=0, sticky="nsew")   
    else:
        toutes_les_pages[index].grid(row=1, column=0, sticky="nsew")   
   
    for i, bouton in enumerate(boutons_widgets):
        if i == index:
            bouton.config(bg='#f2f2f2', fg='#0d1b1e')
        else:
            bouton.config(bg='#0d1b1e', fg='#f2f2f2')


# Liste des boutons de la barre de navigation
boutons = [
    ("Accueil", 0),
    ("Entrées", 1),
    ("Plats", 2),
    ("Desserts", 3),
    ("Boissons", 4),
    ("Paramètres", 5),
]

def creer_commande_bouton(index):
    return lambda: afficher_page_et_surbrillance(index)

# Création des boutons dans barre de navigation
for i, (nom, index) in enumerate(boutons):
    bouton = Button(
        navbar,
        text=nom,
        command= creer_commande_bouton(index),
        bg="#0d1b1e",
        fg="white",
        font=("Arial", 16),
        bd=0,
        relief="flat",
        padx=10,
        pady=5,
    )
    bouton.grid(row=0, column=i, padx=8, pady=5)
    boutons_widgets.append(bouton)

# Affichage de la page Accueil par défaut
afficher_page_et_surbrillance(0)

# Boucle principale de l'application
ma_fenetre.mainloop()