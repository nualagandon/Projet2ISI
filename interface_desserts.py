from interface_categorie import creer_page_categorie

def creer_page_desserts(ma_fenetre, connection):
    return creer_page_categorie(ma_fenetre, "Desserts", connection, "nb_max_desserts")
    