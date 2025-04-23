from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas

def creer_page_plats(ma_fenetre, connexion):
    plats_frame = Frame(ma_fenetre, bg="#f3e0ec")
    plats_frame.grid(row=1, column=0, sticky="nsew")

    # Déclaration de l'objet CategorieRepas
    plats = CategorieRepas("Plats", connexion)

    # Variables liées aux champs de saisie
    reponse_nom_plat = StringVar()
    reponse_nom_etu = StringVar()
    reponse_qt_apportee = StringVar()

    # Fonctions locales
    def charger_plats():
        plats.charger(tableau_plats)
    
    def ajouter_plats():
        nom = reponse_nom_etu.get()
        etu = reponse_nom_etu.get()
        qt = reponse_qt_apportee.get()

        if nom and etu and qt:
            plats.ajouter(nom,etu,qt)
            charger_plats()
            reponse_nom_plat.set("")
            reponse_nom_etu.set("")
            reponse_qt_apportee.set("")
        else:
            print("Veuillez remplir tous les champs")
    
    def supprimer_plat():
        plats.supprimer(tableau_plats)
    
    # Interface
    Label(plats_frame, text="Plats", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    Label(plats_frame, text="Ajouter un plat", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, pady=5)

    Label(plats_frame, text="Nom du plat", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5)
    Entry(plats_frame, textvariable=reponse_nom_plat, width=30).grid(row=2, column=1, padx=5, pady=5)

    Label(plats_frame, text="Nom de l'étudiant", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    Entry(plats_frame, textvariable=reponse_nom_etu, width=30).grid(row=3, column=1, padx=5, pady=5)

    Label(plats_frame, text="Quantité apportée", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=4, column=0, padx=5, pady=5)
    Entry(plats_frame, textvariable=reponse_qt_apportee, width=30).grid(row=4, column=1, padx=5, pady=5)

    Button(plats_frame, text="Ajouter un plat", command=lambda: ajouter_plats(), bg="#a53860", fg="white", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)

    tableau_plats = ttk.Treeview(plats_frame, columns=("nom", "nom_etudiant", "qt_apportee"), show="headings", height=10)
    tableau_plats.heading("nom", text="Nom du plat")
    tableau_plats.heading("nom_etudiant", text="Personne")
    tableau_plats.heading("qt_apportee", text="Quantité")
    tableau_plats.column("nom", width=150, anchor="center")
    tableau_plats.column("nom_etudiant", width=150, anchor="center")
    tableau_plats.column("qt_apportee", width=100, anchor="center")
    tableau_plats.grid(row=6, column=0, columnspan=2, pady=10)

    Button(plats_frame, text="Supprimer un plat", command=lambda: supprimer_plat(), bg="#a53860", fg="white", font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=10)

    charger_plats()

    return plats_frame