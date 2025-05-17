import json
import os
from tkinter import *
from tkinter import messagebox

# Définition du nom de fichier dans lequel les paramètres seront sauvegardés
FICHIER_PARAMETRES = "parametres.json"

# Charger les paramètres depuis le fichier JSON, sinon retourner un dictionnaire vide
def charger_parametres():
    if os.path.exists(FICHIER_PARAMETRES):
        with open(FICHIER_PARAMETRES, "r") as f:
            return json.load(f)
    return {}

# Sauvegarder les paramètres dans le fichier JSON
def sauvegarder_parametres_dans_fichier():
    with open(FICHIER_PARAMETRES, "w") as f:
        json.dump(parametres_sauvegardes, f)

# Initialiser le dictionnaire des paramètres sauvegardés
parametres_sauvegardes = charger_parametres()


def creer_page_parametres(ma_fenetre, connexion):
    global parametres_sauvegardes
    parametres_sauvegardes = charger_parametres()

    parametres_frame = Frame(ma_fenetre, bg="#f3e0ec")
    parametres_frame.grid(row=1, column=0, sticky="new")
    
    # Variables liées aux champs de saisie
    reponse_nb_participants = StringVar(value=str(parametres_sauvegardes.get("nb_participants", 15)))
    parametrage_auto = BooleanVar(value=parametres_sauvegardes.get("parametrage_auto", True))

    reponse_entrees = StringVar(value=str(parametres_sauvegardes.get("nb_max_entrees", "")))
    reponse_plats = StringVar(value=str(parametres_sauvegardes.get("nb_max_plats", "")))
    reponse_desserts = StringVar(value=str(parametres_sauvegardes.get("nb_max_desserts", "")))
    reponse_boissons = StringVar(value=str(parametres_sauvegardes.get("nb_max_boissons", "")))


    # Calcule automatiquement les quantités maximales d’entrées, plats, desserts et boissons en fonction du nombre de participants.
    def initialiser_valeurs():
        try:
            nb_participants = int(reponse_nb_participants.get())
            reponse_entrees.set(int(nb_participants * 0.25))
            reponse_plats.set(int(nb_participants * 0.35))
            reponse_desserts.set(int(nb_participants * 0.25))
            reponse_boissons.set(int(nb_participants * 0.15))
        except ValueError:
            reponse_entrees.set("")
            reponse_plats.set("")
            reponse_desserts.set("")
            reponse_boissons.set("")

    # Active ou désactive les champs de saisie manuelle selon l’état de la case « paramétrage automatique
    def reglage_parametrage_auto():
        etat = "disabled" if parametrage_auto.get() else "normal"
        input_entree.config(state=etat)
        input_plat.config(state=etat)
        input_dessert.config(state=etat)
        input_boisson.config(state=etat)

        if parametrage_auto.get():
            initialiser_valeurs()
        else:
            reponse_entrees.set(parametres_sauvegardes.get("nb_max_entrees", ""))
            reponse_plats.set(parametres_sauvegardes.get("nb_max_plats", ""))
            reponse_desserts.set(parametres_sauvegardes.get("nb_max_desserts", ""))
            reponse_boissons.set(parametres_sauvegardes.get("nb_max_boissons", ""))

    # Met à jour les quantités si le nombre de participants change et si le mode automatique est activé        
    def on_nb_participants_change(*args):
         if parametrage_auto.get():
            initialiser_valeurs()

    # Supprime toutes les donées des tables de la base de données et réinitialise les paramètres et sauvegarde dans le fichier JSON
    def reinitialiser():
        if messagebox.askyesno("Confirmation de réinitialisation", "⚠️ ATTENTION : tout sera supprimé. Voulez-vous continuer ?"):
            curs = connexion.cursor()
            curs.executescript("DELETE FROM Entrees; DELETE FROM Plats; DELETE FROM Desserts; DELETE FROM Boissons;")
            curs.close()

            reponse_nb_participants.set("15")
            parametrage_auto.set(True)
            initialiser_valeurs()
            reglage_parametrage_auto()

            parametres_sauvegardes.update({
                "nb_participants": 15,
                "parametrage_auto": True,
                "nb_max_entrees": int(reponse_entrees.get()),
                "nb_max_plats": int(reponse_plats.get()),
                "nb_max_desserts": int(reponse_desserts.get()),
                "nb_max_boissons": int(reponse_boissons.get()),
            })

            sauvegarder_parametres_dans_fichier()
            messagebox.showinfo("Réinitialisation réussie", "Toutes les données ont été supprimées et les paramètres réinitialisés.")

    # Sauvegarde les paramètres dans le fichier JSON et vérifie les erreurs
    def sauvegarder_parametres():
        try:
            nb_participants = int(reponse_nb_participants.get())
            nb_max_entrees = int(reponse_entrees.get())
            nb_max_plats = int(reponse_plats.get())
            nb_max_desserts = int(reponse_desserts.get())
            nb_max_boissons = int(reponse_boissons.get())

            # Vérifications
            curs = connexion.cursor()
            erreurs = []

            def verif_table(table, nb_max, nom):
                curs.execute(f"SELECT SUM(qt_apportee) FROM {table};")
                nb_enregistre = curs.fetchone()[0] or 0
                if nb_max < nb_enregistre:
                    erreurs.append(f"Le nombre de {nom} est inférieur à ce qui est déjà enregistré.")
                return nb_enregistre

            verif_table("Entrees", nb_max_entrees, "d'entrées")
            verif_table("Plats", nb_max_plats, "de plats")
            verif_table("Desserts", nb_max_desserts, "de desserts")
            verif_table("Boissons", nb_max_boissons, "de boissons")
            curs.close()

            if any(val < 0 for val in [nb_max_entrees, nb_max_plats, nb_max_desserts, nb_max_boissons]):
                erreurs.append("Les quantités doivent être positives.")

            if erreurs:
                messagebox.showerror("Erreur de sauvegarde", "\n".join(erreurs))
                return

            parametres_sauvegardes.update({
                "nb_participants": nb_participants,
                "parametrage_auto": parametrage_auto.get(),
                "nb_max_entrees": nb_max_entrees,
                "nb_max_plats": nb_max_plats,
                "nb_max_desserts": nb_max_desserts,
                "nb_max_boissons": nb_max_boissons,
            })

            sauvegarder_parametres_dans_fichier()
            messagebox.showinfo("Sauvegarde réussie", "Les paramètres ont été sauvegardés avec succès.")

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    
    # Lie le champ de nombre de participants à une fonction qui s'execute à chaque fois que la valeur change
    reponse_nb_participants.trace_add("write", on_nb_participants_change)

    # Création de l'interface graphique

    Label(parametres_frame, 
          text="Paramètres", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 28,"bold")
          ).pack(pady=(10, 5))
    
    form_frame = Frame(parametres_frame, bg="#f3e0ec", bd=2, relief="groove")
    form_frame.pack(pady=10, padx=20, fill="x")
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)

    Label(form_frame, 
          text="Nombre de participants",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)
          ).grid(row=0, column=1, padx=10, pady=5, sticky="e")
    
    Entry(form_frame,
          textvariable=reponse_nb_participants,
          width=30
          ).grid(row=0, column=2, padx=10, pady=5, sticky="w")
    
    Checkbutton(form_frame,
                text="Paramétrage automatique",
                variable=parametrage_auto,
                command = reglage_parametrage_auto,
                bg="#f3e0ec",
                fg="#450920",
                font=("Arial", 14)
                ).grid(row=1, column=1, columnspan=2, pady=(10, 15))
    
    Label(form_frame,
          text="Entrées",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=5, sticky="e")
    input_entree = Entry(form_frame,
          textvariable=reponse_entrees,
          width=30, state="disabled")
    input_entree.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    
    Label(form_frame,
          text="Plats",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=3, column=1, padx=10, pady=5, sticky="e")
    input_plat = Entry(form_frame,
          textvariable=reponse_plats,
          width=30, state="disabled")
    input_plat.grid(row=3, column=2, padx=10, pady=5, sticky="w")

    Label(form_frame,
          text="Desserts",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=4, column=1, padx=10, pady=5, sticky="e")
    input_dessert = Entry(form_frame,
          textvariable=reponse_desserts,
          width=30, state="disabled")
    input_dessert.grid(row=4, column=2, padx=10, pady=5, sticky="w")
    
    Label(form_frame,
          text="Boissons",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=5, column=1, padx=10, pady=5, sticky="e")
    input_boisson = Entry(form_frame,
          textvariable=reponse_boissons,
          width=30, state="disabled")
    input_boisson.grid(row=5, column=2, padx=10, pady=5, sticky="w")
    
    boutons_frame = Frame(parametres_frame, bg="#f3e0ec")
    boutons_frame.pack(pady=(10, 0))

    # Bouton pour sauvegarder les paramètres saisis
    Button(boutons_frame,
           text="Sauvegarder le paramétrage",
           command=sauvegarder_parametres,
           bg="#a53860",
           fg="white", relief="raised",
           font=("Arial", 14)).pack(side="left", padx=10)
    
    # Bouton pour tout réinitialiser (après confirmation)
    Button(boutons_frame,
           text="Réinitialiser",
           command=reinitialiser,
           bg="#a53860",
           fg="white", relief="raised",
           font=("Arial", 14)).pack(side="left", padx=10)
    
    # Initialiser le paramétrage automatique au chargement de la page
    reglage_parametrage_auto()

    return parametres_frame
          