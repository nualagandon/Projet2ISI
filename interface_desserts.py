from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes

def creer_page_desserts(ma_fenetre, connection):
    desserts_frame = Frame(ma_fenetre, bg="#f3e0ec")
    desserts_frame.grid(row=1, column=0, sticky="nsew")

    # Déclaration de l'objet CategorieRepas
    desserts = CategorieRepas("desserts", connection)

    # Variables liées aux champs de saisie
    reponse_nom_dessert = StringVar()
    reponse_nom_etudiant_dessert = StringVar()
    reponse_qt_dessert_apportee = StringVar()

    # Fonctions locales
    def charger_desserts():
        desserts.charger(tableau_desserts)

    def ajouter_dessert():
        nom = reponse_nom_dessert.get()
        etu = reponse_nom_etudiant_dessert.get()
        qt = reponse_qt_dessert_apportee.get()

        if not nom or not etu or not qt:
            print("Veuillez remplir tous les champs.")
            return
        
        try:
            qt = int(qt)
        except ValueError:
            print("La quantité doit être un nombre entier.")
            return
        
        total_desserts = sum(
            int(tableau_desserts.item(item, "values")[2]) for item in tableau_desserts.get_children()
        )

        limite_desserts = parametres_sauvegardes.get("nb_max_desserts", 0)
        
        if total_desserts + qt > limite_desserts:
            print(f"Limite atteinte pour les desserts ({limite_desserts}). Vous ne pouvez pas ajouter plus de desserts.")
            return
    
    
        desserts.ajouter(nom, etu, qt)
        charger_desserts()
        reponse_nom_dessert.set("")
        reponse_nom_etudiant_dessert.set("")
        reponse_qt_dessert_apportee.set("")

    def supprimer_dessert():
        desserts.supprimer(tableau_desserts)

    # Interface
    Label(desserts_frame, text="Entrées", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    Label(desserts_frame, text="Ajouter un Dessert", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, pady=5)

    Label(desserts_frame, text="Nom du dessert", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5)
    Entry(desserts_frame, textvariable=reponse_nom_dessert, width=30).grid(row=2, column=1, padx=5, pady=5)

    Label(desserts_frame, text="Nom de l'étudiant", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    Entry(desserts_frame, textvariable=reponse_nom_etudiant_dessert, width=30).grid(row=3, column=1, padx=5, pady=5)

    Label(desserts_frame, text="Quantité apportée", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=4, column=0, padx=5, pady=5)
    Entry(desserts_frame, textvariable=reponse_qt_dessert_apportee, width=30).grid(row=4, column=1, padx=5, pady=5)

    Button(desserts_frame, text="Ajouter un dessert", command=ajouter_dessert, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)

    tableau_desserts = ttk.Treeview(desserts_frame, columns=("nom", "nom_etudiant", "qt_apportee"), show="headings", height=10)
    tableau_desserts.heading("nom", text="Nom du plat")
    tableau_desserts.heading("nom_etudiant", text="Personne")
    tableau_desserts.heading("qt_apportee", text="Quantité")
    tableau_desserts.column("nom", width=150, anchor="center")
    tableau_desserts.column("nom_etudiant", width=150, anchor="center")
    tableau_desserts.column("qt_apportee", width=100, anchor="center")
    tableau_desserts.grid(row=6, column=0, columnspan=2, pady=10)

    Button(desserts_frame, text="Supprimer une entrée", command=supprimer_dessert, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=10)

    charger_desserts()

    return desserts_frame