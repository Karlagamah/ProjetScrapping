from app.scraper.amazon_scraper import recuperer_page
from app.scraper.parsing import extraire_produits
from app.views.console_view import afficher_produits


def lancer(URL):
    soup = recuperer_page(URL)
    liste = extraire_produits(soup)
    afficher_produits(liste)
    return liste
