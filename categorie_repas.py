class CategorieRepas:
    def __init__(self, nom_table, connexion):
        self.nom_table = nom_table
        self.connexion = connexion
    
    def charger(self, tableau):
        tableau.delete(*tableau.get_children())
        curs = self.connexion.cursor()
        requete = f"SELECT id, nom, nom_etudiant, qt_apportee FROM {self.nom_table}"
        for row in curs.execute(requete):
            tableau.insert("", "end", values=row[1:], iid=row[0])
    
    def ajouter(self, nom, nom_etudiant, qt_apportee):
        curs = self.connexion.cursor()
        requete = f"INSERT INTO {self.nom_table} (nom, nom_etudiant, qt_apportee) VALUES (?, ?, ?)"
        curs.execute(requete, (nom, nom_etudiant, qt_apportee))
        self.connexion.commit()

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
