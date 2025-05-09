from tkinter import *
from tkinter import ttk
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes

def creer_page_entrees(ma_fenetre, connection):
    entrees_frame = Frame(ma_fenetre, bg="#f3e0ec")
    entrees_frame.grid(row=1, column=0, sticky="nsew")

    # Déclaration de l'objet CategorieRepas
    entrees = CategorieRepas("Entrees", connection)

    # Variables liées aux champs de saisie
    reponse_nom_entree = StringVar()
    reponse_nom_etudiant_entree = StringVar()
    reponse_qt_entree_apportee = StringVar()

    # Fonctions locales
    def charger_entrees():
        entrees.charger(tableau_entrees)

    def ajouter_entree():
        nom = reponse_nom_entree.get()
        etu = reponse_nom_etudiant_entree.get()
        qt = reponse_qt_entree_apportee.get()

        if not nom or not etu or not qt:
            print("Veuillez remplir tous les champs.")
            return
        
        total_entrees = sum(
            int(tableau_entrees.item(item, "values")[2]) for item in tableau_entrees.get_children()
        )
        
        limite_entrees = parametres_sauvegardes.get("nb_max_entrees", 0)

        if total_entrees >= limite_entrees:
            print(f"Limite atteinte pour les entrées ({limite_entrees}). Vous ne pouvez pas ajouter plus d'entrées.")
            return 
        
        entrees.ajouter(nom, etu, qt)
        charger_entrees()
        reponse_nom_entree.set("")
        reponse_nom_etudiant_entree.set("")
        reponse_qt_entree_apportee.set("")
        

    def supprimer_entree():
        entrees.supprimer(tableau_entrees)

    # Interface
    Label(entrees_frame, text="Entrées", bg="#f3e0ec", fg="#450920", font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10)

    Label(entrees_frame, text="Ajouter une entrée", bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=1, column=0, columnspan=2, pady=5)

    Label(entrees_frame, text="Nom du plat", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=2, column=0, padx=5, pady=5)
    Entry(entrees_frame, textvariable=reponse_nom_entree, width=30).grid(row=2, column=1, padx=5, pady=5)

    Label(entrees_frame, text="Nom de l'étudiant", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    Entry(entrees_frame, textvariable=reponse_nom_etudiant_entree, width=30).grid(row=3, column=1, padx=5, pady=5)

    Label(entrees_frame, text="Quantité apportée", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=4, column=0, padx=5, pady=5)
    Entry(entrees_frame, textvariable=reponse_qt_entree_apportee, width=30).grid(row=4, column=1, padx=5, pady=5)

    Button(entrees_frame, text="Ajouter une entrée", command=ajouter_entree, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)

    tableau_entrees = ttk.Treeview(entrees_frame, columns=("nom", "nom_etudiant", "qt_apportee"), show="headings", height=10)
    tableau_entrees.heading("nom", text="Nom du plat")
    tableau_entrees.heading("nom_etudiant", text="Personne")
    tableau_entrees.heading("qt_apportee", text="Quantité")
    tableau_entrees.column("nom", width=150, anchor="center")
    tableau_entrees.column("nom_etudiant", width=150, anchor="center")
    tableau_entrees.column("qt_apportee", width=100, anchor="center")
    tableau_entrees.grid(row=6, column=0, columnspan=2, pady=10)

    Button(entrees_frame, text="Supprimer une entrée", command=supprimer_entree, bg="#a53860", fg="white", font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=10)

    charger_entrees()

    return entrees_frame