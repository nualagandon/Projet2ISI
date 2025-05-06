from tkinter import *

parametres_sauvegardes = {}

def creer_page_parametres(ma_fenetre):
    global parametres_sauvegardes

    parametres_frame = Frame(ma_fenetre, bg="#f3e0ec")
    parametres_frame.grid(row=1, column=0, sticky="nsew")

    # Variables liées aux champs de saisie
    reponse_nb_participants = StringVar(value="15")
    parametrage_auto = BooleanVar(value=True)
    reponse_entrees = StringVar()
    reponse_plats = StringVar()
    reponse_desserts = StringVar()
    reponse_boissons = StringVar()
    
    def sauvegarder_parametres():
        try:
            parametres_sauvegardes["nb_participants"] = int(reponse_nb_participants.get())
            parametres_sauvegardes["nb_max_entrees"] = int(reponse_entrees.get())
            parametres_sauvegardes["nb_max_plats"] = int(reponse_plats.get())
            parametres_sauvegardes["nb_max_desserts"] = int(reponse_desserts.get())
            parametres_sauvegardes["nb_max_boissons"] = int(reponse_boissons.get())
            print("Paramètres sauvegardés :", parametres_sauvegardes)
        except ValueError:
            print("Erreur : Veuillez entrer des valeurs valides.")

    # Initialisation des valeurs du paramétrage automatique
    def initialiser_valeurs():
        try:
            nb_participants = int(reponse_nb_participants.get())
            reponse_entrees.set(int(nb_participants * 0.25))
            reponse_plats.set(int(nb_participants * 0.35))
            reponse_desserts.set(int(nb_participants * 0.25))
            reponse_boissons.set(int(nb_participants * 0.15))
            sauvegarder_parametres()
        except ValueError:
            reponse_entrees.set("")
            reponse_plats.set("")
            reponse_desserts.set("")
            reponse_boissons.set("")

    # Fonction pour le paramétrage automatique
    def reglage_parametrage_auto():
        if parametrage_auto.get():
            initialiser_valeurs()
            # Désactiver les champs d'entrée
            input_entree.config(state="disabled")
            input_plat.config(state="disabled")
            input_dessert.config(state="disabled")
            input_boisson.config(state="disabled")
        else:
            # Désactiver les champs d'entrée
            input_entree.config(state="normal")
            input_plat.config(state="normal")
            input_dessert.config(state="normal")
            input_boisson.config(state="normal")

    # Interface
    Label(parametres_frame, 
          text="Paramètres", 
          bg="#f3e0ec", 
          fg="#450920", 
          font=("Arial", 28)).grid(row=0, column=0, columnspan=2, pady=10) 

    Label(parametres_frame, 
          text="Nombre de participants",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=1, column=0, padx=5, pady=5)
    
    Entry(parametres_frame,
          textvariable=reponse_nb_participants,
          width=30).grid(row=1, column=1, padx=5, pady=5)
    
    Checkbutton(parametres_frame,
                text="Paramétrage automatique",
                variable=parametrage_auto,
                command = reglage_parametrage_auto,
                bg="#f3e0ec",
                fg="#450920",
                font=("Arial", 14)).grid(row=2, column=0, columnspan=2, pady=5)
    
    Label(parametres_frame,
          text="Entrées",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    input_entree = Entry(parametres_frame,
          textvariable=reponse_entrees,
          width=30, state="disabled")
    input_entree.grid(row=3, column=1, padx=5, pady=5)
    
    Label(parametres_frame,
          text="Plats",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=4, column=0, padx=5, pady=5)
    input_plat = Entry(parametres_frame,
          textvariable=reponse_plats,
          width=30, state="disabled")
    input_plat.grid(row=4, column=1, padx=5, pady=5)

    Label(parametres_frame,
          text="Desserts",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=5, column=0, padx=5, pady=5)
    input_dessert = Entry(parametres_frame,
          textvariable=reponse_desserts,
          width=30, state="disabled")
    input_dessert.grid(row=5, column=1, padx=5, pady=5)
    
    Label(parametres_frame,
          text="Boissons",
          bg="#f3e0ec",
          fg="#450920",
          font=("Arial", 14)).grid(row=6, column=0, padx=5, pady=5)
    input_boisson = Entry(parametres_frame,
          textvariable=reponse_boissons,
          width=30, state="disabled")
    input_boisson.grid(row=6, column=1, padx=5, pady=5)
    
    Button(parametres_frame,
           text="Sauvegarder le paramétrage",
           command=sauvegarder_parametres,
           bg="#450920",
           fg="white",
           font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=10)
    
    # Initialiser le paramétrage automatique au chargement de la page
    initialiser_valeurs()

    return parametres_frame
          