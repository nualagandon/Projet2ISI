import sqlite3

# Connexion à la base de données SQLite
def connecter_bd():
    try:
        connexion = sqlite3.connect("repas.db")
        return connexion
    except sqlite3.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None

# Création des tables dans la base de données si elles n'existent pas
def creer_tables(connexion):
    try:
        curs = connexion.cursor()

        tables = ["Entrees", "Plats", "Desserts", "Boissons"]
        for table in tables:
            curs.execute(f'''
                CREATE TABLE IF NOT EXISTS {table} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    nom_etudiant TEXT NOT NULL,
                    qt_apportee INTEGER NOT NULL
                )
            ''')

        connexion.commit()
        print("Tables créées avec succès.")
    except sqlite3.Error as e:
        print(f"Erreur lors de la création des tables : {e}")