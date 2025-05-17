# Définition de la classe CategorieRepas qui gère les données d'une table de la base liée à une catégorie de repas
class CategorieRepas:
    def __init__(self, nom_table, connexion):
        self.nom_table = nom_table  # Nom de la table à manipuler (ex. : "entrees", "plats")
        self.connexion = connexion  # Connexion à la base de données
    
    # Méthode pour charger les données de la table dans un tableau (ex. : Treeview de Tkinter)
    def charger(self, tableau):
        tableau.delete(*tableau.get_children()) # Nettoyage du tableau (suppression des anciennes lignes)
        curs = self.connexion.cursor()          # Création du curseur pour exécuter les requêtes SQL
        requete = f"SELECT id, nom, nom_etudiant, qt_apportee FROM {self.nom_table}"  # Sélection des colonnes utiles
        for row in curs.execute(requete):       # Parcours des résultats de la requête
            # Insertion des données dans le tableau
            tableau.insert("", "end", values=row[1:], iid=row[0])
    
    # Méthode pour ajouter une nouvelle entrée dans la table
    def ajouter(self, nom, nom_etudiant, qt_apportee):
        curs = self.connexion.cursor()
        requete = f"INSERT INTO {self.nom_table} (nom, nom_etudiant, qt_apportee) VALUES (?, ?, ?)"
        curs.execute(requete, (nom, nom_etudiant, qt_apportee))
        self.connexion.commit()

    # Méthode pour supprimer un élément sélectionné dans le tableau (et la base)
    def supprimer(self, tableau):
        item_selectionne = tableau.selection()
        if not item_selectionne:
            print("Aucun élément sélectionné.")
            return
        valeurs = tableau.item(item_selectionne)["values"]
        requete = f"DELETE FROM {self.nom_table} WHERE nom=? AND nom_etudiant=? AND qt_apportee=?"
        self.connexion.cursor().execute(requete, tuple(valeurs))
        self.connexion.commit()
        tableau.delete(item_selectionne)
