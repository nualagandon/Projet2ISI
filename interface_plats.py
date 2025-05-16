from interface_categorie import creer_page_categorie

def creer_page_plats(ma_fenetre, connexion):
    return creer_page_categorie(ma_fenetre, "Plats", connexion, "nb_max_plats")