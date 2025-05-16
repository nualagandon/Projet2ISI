from tkinter import *
from tkinter import messagebox

parametres_sauvegardes = {}

def creer_page_parametres(ma_fenetre, connexion):
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

    #Fonction pour réinitialiser la base de données 
    def reinitialiser() :
            curs = connexion.cursor()
            requete = "delete from Entrees; delete from Plats; delete from Desserts; delete from Boissons;"
            curs.executescript(requete)
            curs.close()
    
    def sauvegarder_parametres(afficher_message=True):
      #on vérifie si les quantités sont bonnes. 
      #on récupère d'abord les données déjà incluses dans la base de données
      #On récupère le nombre de plats enregistré dans la base
      curs = connexion.cursor()
      requete = "select sum(qt_apportee) from Entrees;"
      curs.execute(requete)
      nb_entrees = curs.fetchone()[0] or 0
      requete = "select sum(qt_apportee) from Plats;"
      curs.execute(requete)
      nb_plats = curs.fetchone()[0] or 0
      requete = "select sum(qt_apportee) from Desserts;"
      curs.execute(requete)
      nb_desserts = curs.fetchone()[0] or 0
      requete = "select sum(qt_apportee) from Boissons;"
      curs.execute(requete)
      nb_boissons = curs.fetchone()[0] or 0
      curs.close()

      #On vérifie qu'il n'y a pas de problème avec les quantités enregistrées et celles présentent dans la base
      try:  
            parametres_sauvegardes["nb_participants"] = int(reponse_nb_participants.get())

            if (int(reponse_entrees.get()) >= nb_entrees) :
                  parametres_sauvegardes["nb_max_entrees"] = int(reponse_entrees.get())
            else : 
                 #on empêche l'affichage de l'enregistrement complet des valeurs.
                 afficher_message = False
                 #on prévient l'utilisateur.
                 messagebox.showerror("Erreur de sauvegarde", "Le nombre d'entrées demandé est inférieur au nombre d'entrées déjà présent.")

            if (int(reponse_plats.get()) >= nb_plats) :
                  parametres_sauvegardes["nb_max_plats"] = int(reponse_plats.get())
            else : 
                 #on empêche l'affichage de l'enregistrement complet des valeurs.
                 afficher_message = False
                 #on prévient l'utilisateur.
                 messagebox.showerror("Erreur de sauvegarde", "Le nombre de plat demandé est inférieur au nombre de plats déjà présent.")
            
            if (int(reponse_desserts.get()) >= nb_desserts) :
                  parametres_sauvegardes["nb_max_desserts"] = int(reponse_desserts.get())
            else : 
                 #on empêche l'affichage de l'enregistrement complet des valeurs.
                 afficher_message = False
                 #on prévient l'utilisateur.
                 messagebox.showerror("Erreur de sauvegarde", "Le nombre de desserts demandé est inférieur au nombre de desserts déjà présent.")
            
            if(int(reponse_boissons.get()) >= nb_boissons) :
                  parametres_sauvegardes["nb_max_boissons"] = int(reponse_boissons.get())
            else : 
                 #on empêche l'affichage de l'enregistrement complet des valeurs.
                 afficher_message = False
                 #on prévient l'utilisateur.
                 messagebox.showerror("Erreur de sauvegarde", "Le nombre de boissons demandé est inférieur au nombre de boissons déjà présent.")

            if afficher_message:
                  messagebox.showinfo("Sauvegarde réussie", "Les paramètres ont été sauvegardés avec succès.")
      except ValueError:
            if afficher_message:
                  messagebox.showerror("Erreur de sauvegarde", "Veuillez entrer des valeurs valides.")

    # Initialisation des valeurs du paramétrage automatique
    def initialiser_valeurs():
        try:
            nb_participants = int(reponse_nb_participants.get())
            reponse_entrees.set(int(nb_participants * 0.25))
            reponse_plats.set(int(nb_participants * 0.35))
            reponse_desserts.set(int(nb_participants * 0.25))
            reponse_boissons.set(int(nb_participants * 0.15))
            sauvegarder_parametres(afficher_message=False)
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
    
    Button(parametres_frame,
           text="Réinitialiser",
           command=reinitialiser,
           bg="#450920",
           fg="white",
           font=("Arial", 14)).grid(row=8, column=2, pady=10)
    
    # Initialiser le paramétrage automatique au chargement de la page
    initialiser_valeurs()

    return parametres_frame
          