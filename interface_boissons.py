from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes

def creer_page_boissons(ma_fenetre, connection):
    boissons_frame = Frame(ma_fenetre, bg="#f3e0ec")
    boissons_frame.grid(row=1, column=0, sticky="nsew")

    # Déclaration de l'objet CategorieRepas
    boissons = CategorieRepas("Boissons", connection)

    # Variables liées aux champs de saisie
    reponse_nom_boisson = StringVar()
    reponse_nom_etu = StringVar()
    reponse_qt_boisson = StringVar()

    # Fonctions locales
    def charger_boissons():
        boissons.charger(tableau_boissons)

    def ajouter_boisson():
        nom = reponse_nom_boisson.get()
        etu = reponse_nom_etu.get()
        qt = reponse_qt_boisson.get()
        
        if not nom or not etu or not qt:
            print("Veuillez remplir tous les champs.")
            return
        
        try:
            qt = int(qt)
        except ValueError:
            print("La quantité doit être un nombre entier.")
            return
        
        total_boissons = sum(
            int(tableau_boissons.item(item, "values")[2]) for item in tableau_boissons.get_children()
        )

        limite_boissons = parametres_sauvegardes.get("nb_max_boissons", 0)

        if total_boissons + qt > limite_boissons:
            print(f"Limite atteinte pour les boissons ({limite_boissons}). Vous ne pouvez pas ajouter plus de boissons.")
            return
        
        
        boissons.ajouter(nom, etu, qt)
        charger_boissons()
        reponse_nom_boisson.set("")
        reponse_nom_etu.set("")
        reponse_qt_boisson.set("")


    def supprimer_boissons():
        boissons.supprimer(tableau_boissons)

    # Interface
    Label(boissons_frame, text="Boissons", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    Label(boissons_frame, text="Ajouter une boisson", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, pady=5)

    Label(boissons_frame, text="Nom du plat", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5)
    Entry(boissons_frame, textvariable=reponse_nom_boisson, width=30).grid(row=2, column=1, padx=5, pady=5)

    Label(boissons_frame, text="Nom de l'étudiant", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    Entry(boissons_frame, textvariable=reponse_nom_etu, width=30).grid(row=3, column=1, padx=5, pady=5)

    Label(boissons_frame, text="Quantité apportée", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=4, column=0, padx=5, pady=5)
    Entry(boissons_frame, textvariable=reponse_qt_boisson, width=30).grid(row=4, column=1, padx=5, pady=5)

    Button(boissons_frame, text="Ajouter une boisson", command=ajouter_boisson, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)

    tableau_boissons = ttk.Treeview(boissons_frame, columns=("nom", "nom_etudiant", "qt_apportee"), show="headings", height=10)
    tableau_boissons.heading("nom", text="Nom de la boisson")
    tableau_boissons.heading("nom_etudiant", text="Personne")
    tableau_boissons.heading("qt_apportee", text="Quantité")
    tableau_boissons.column("nom", width=150, anchor="center")
    tableau_boissons.column("nom_etudiant", width=150, anchor="center")
    tableau_boissons.column("qt_apportee", width=100, anchor="center")
    tableau_boissons.grid(row=6, column=0, columnspan=2, pady=10)

    Button(boissons_frame, text="Supprimer une boisson", command=supprimer_boissons, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=10)

    charger_boissons()

    return boissons_frame