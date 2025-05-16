from interface_categorie import creer_page_categorie

def creer_page_entrees(ma_fenetre, connexion):
    return creer_page_categorie(ma_fenetre, "Entrees", connexion, "nb_max_entrees")