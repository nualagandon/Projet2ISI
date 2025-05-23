from tkinter import *
from tkinter import ttk
from database import connecter_bd, creer_tables
from interface_entrees import creer_page_entrees
from interface_plats import creer_page_plats
from interface_desserts import creer_page_desserts
from interface_boissons import creer_page_boissons
from interface_parametres import creer_page_parametres
from interface_accueil import creer_page_accueil

# Connexion à la base de données
connexion = connecter_bd()
if connexion:
    creer_tables(connexion) # Crée les tables si la connexion est réussie
else:
    print("Échec de la connexion à la base de données.")    # Message d'erreur
    exit()  # Quitte le programme si la connexion échoue

# Création de la fenêtre principale
ma_fenetre = Tk()
ma_fenetre.title("Organisation des repas")
ma_fenetre.geometry("1000x800")     # Dimension de la fenêtre
ma_fenetre.resizable(False, False)  # Fenetre non redimensionnable

# Personnalisation de la couleur des barres de progression
style = ttk.Style()
style.theme_use("default")
style.configure("pink.Horizontal.TProgressbar", troughcolor="white", background="#a53860", bordercolor="#a53860")


# Création des pages correspondant à chaque section de l'application
entrees_frame = creer_page_entrees(ma_fenetre, connexion)
plats_frame = creer_page_plats(ma_fenetre, connexion)
desserts_frame = creer_page_desserts(ma_fenetre, connexion)
boissons_frame = creer_page_boissons(ma_fenetre, connexion)
accueil_frame = creer_page_accueil(ma_fenetre, connexion)
parametres_frame = creer_page_parametres(ma_fenetre, connexion)

# Liste contenant toutes les pages de l'application
toutes_les_pages = [accueil_frame, entrees_frame, plats_frame, desserts_frame, boissons_frame, parametres_frame]

# Configuration de la grille principale pour que la page s'étende correctement
ma_fenetre.rowconfigure(1, weight=1)
ma_fenetre.columnconfigure(0, weight=1)

# Création de la barre de navigation supérieure

navbar_frame = Frame(ma_fenetre, bg="#0d1b1e")
navbar_frame.grid(row=0, column=0, sticky="ew") # Positionnement de la barre de navigation en haut, occupant toute la largeur
navbar_frame.grid_columnconfigure(0, weight=1)  
navbar_frame.grid_columnconfigure(1, weight=0)

navbar = Frame(navbar_frame, bg="#0d1b1e", height=50)   # Frame contenant la barre de navigation
navbar.grid(row=0, column=0, sticky="e")                  # alginée à droite

# Suivi des boutons de la barre de navigation
boutons_widgets = []

# Fonction pour changer de page (et recréer la page à chaque fois pour rafraichir les données si besoin))
def afficher_page_et_surbrillance(index):
    global parametres_frame
    global accueil_frame
    global entrees_frame
    global plats_frame
    global boissons_frame
    global desserts_frame

    # Masquer toutes les pages existantes
    for frame in toutes_les_pages:
        frame.grid_forget()

    # Recréer dynamiquement la page correspondant à l’index
    if index == 0:
        accueil_frame = creer_page_accueil(ma_fenetre, connexion)
        toutes_les_pages[0] = accueil_frame
    elif index == 1:
        entrees_frame = creer_page_entrees(ma_fenetre, connexion)
        toutes_les_pages[1] = entrees_frame
    elif index == 2:
        plats_frame = creer_page_plats(ma_fenetre, connexion)
        toutes_les_pages[2] = plats_frame
    elif index == 3:
        desserts_frame = creer_page_desserts(ma_fenetre, connexion)
        toutes_les_pages[3] = desserts_frame
    elif index == 4:
        boissons_frame = creer_page_boissons(ma_fenetre, connexion)
        toutes_les_pages[4] = boissons_frame
    elif index == 5:
        parametres_frame = creer_page_parametres(ma_fenetre, connexion)
        toutes_les_pages[5] = parametres_frame

    # Afficher la page sélectionnée
    toutes_les_pages[index].grid(row=1, column=0, sticky="nsew")

# Liste des boutons de la barre de navigation
boutons = [
    ("Accueil", 0),
    ("Entrées", 1),
    ("Plats", 2),
    ("Desserts", 3),
    ("Boissons", 4),
    ("Paramètres", 5),
]

# Fonction intermédiaire pour éviter les erreurs liées aux boucles et lambdas
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