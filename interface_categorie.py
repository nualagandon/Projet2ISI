from tkinter import *
from tkinter import ttk, messagebox
from categorie_repas import CategorieRepas
from interface_parametres import parametres_sauvegardes


def creer_page_categorie(ma_fenetre, nom_categorie, connexion, nom_parametre_max):
   
    frame = Frame(ma_fenetre, bg="#f3e0ec")
    frame.grid(row=1, column=0, sticky="nsew")

    categorie = CategorieRepas(nom_categorie, connexion)

    reponse_nom = StringVar()
    reponse_nom_etu = StringVar()
    reponse_qt = StringVar()

    def charger():
        categorie.charger(tableau)
    
    def ajouter():
        nom = reponse_nom.get().strip()
        etu = reponse_nom_etu.get().strip()
        qt = reponse_qt.get().strip()

        if not nom or not etu or not qt:
            messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
            return

        try:
            qt = int(qt)
        except ValueError:
            messagebox.showerror("Quantité invalide", "La quantité doit être un entier strictement positif.")
            return

        total = sum(
            int(tableau.item(item, "values")[2]) for item in tableau.get_children()
        )

        limite = parametres_sauvegardes.get(nom_parametre_max, 0)

        if total + qt > limite:
            messagebox.showerror("Limite atteinte", f"Limite atteinte pour les {nom_categorie.lower()} ({limite}).")
            return

        categorie.ajouter(nom, etu, qt)
        charger()
        reponse_nom.set("")
        reponse_nom_etu.set("")
        reponse_qt.set("")

    def supprimer():
        categorie.supprimer(tableau)
        charger()

    # Interface
    Label(frame, text=nom_categorie, bg="#f3e0ec", fg="#450920", font=("Arial", 28, "bold")
          ).pack(pady=(20, 10))
    
    form_frame = Frame(frame, bg="#f3e0ec", bd=2, relief="groove")
    form_frame.pack(pady=10, padx=20, fill="x", expand=True)

    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)
    
    Label(form_frame, text=f"Ajouter un(e) {nom_categorie[:-1].lower()}",bg="#f3e0ec", fg="#450920", font=("Arial", 18)).grid(row=0, column=1, columnspan=2, pady=(10, 15))

    Label(form_frame, text=f"Nom du {nom_categorie[:-1].lower()}", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=1, column=1, padx=10, pady=5, sticky="e")
    Entry(form_frame, textvariable=reponse_nom, width=30).grid(row=1, column=2, padx=10, pady=5, sticky="w")

    Label(form_frame, text="Nom de l'étudiant", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=5, sticky="e")
    Entry(form_frame, textvariable=reponse_nom_etu, width=30).grid(row=2, column=2, padx=10, pady=5, sticky="w")

    Label(form_frame, text="Quantité apportée", bg="#f3e0ec", fg="#450920", font=("Arial", 14)).grid(row=3, column=1, padx=10, pady=5, sticky="e")
    Entry(form_frame, textvariable=reponse_qt, width=30).grid(row=3, column=2, padx=10, pady=5, sticky="w")

    Button(form_frame, text=f"Ajouter un(e) {nom_categorie[:-1].lower()}",command=ajouter, bg="#a53860", fg="white", font=("Arial", 14), relief="raised").grid(row=4, column=1, columnspan=2, pady=(15, 10))


    # Tableau
    tableau_frame = Frame(frame, bg="#f3e0ec")
    tableau_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#fff", foreground="#450920", rowheight=28)
    style.configure("Custom.Treeview.Heading", background="#a53860", foreground="white", font=("Arial", 12, "bold"))
    
    tableau = ttk.Treeview(
        tableau_frame, columns=("nom", "nom_etudiant", "qt_apportee"),
        show="headings", height=10, style="Custom.Treeview"
    )

    tableau.heading("nom", text="Nom")
    tableau.heading("nom_etudiant", text="Personne")
    tableau.heading("qt_apportee", text="Quantité")
    tableau.column("nom", width=150, anchor="center")
    tableau.column("nom_etudiant", width=150, anchor="center")
    tableau.column("qt_apportee", width=100, anchor="center")
    tableau.pack(fill="both", expand=True)

    Button(frame, text=f"Supprimer un(e) {nom_categorie[:-1].lower()}", command=supprimer, bg="#a53860", fg="white", font=("Arial", 14), relief="raised").pack(pady=(10, 20))

    charger()

    return frame
