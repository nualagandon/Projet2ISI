from interface_categorie import creer_page_categorie

def creer_page_boissons(ma_fenetre, connection):
   return creer_page_categorie(ma_fenetre, "Boissons", connection, "nb_max_boissons")