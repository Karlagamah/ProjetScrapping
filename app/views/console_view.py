def afficher_produits(liste):
    for p in liste:
        print("nom : ", p["nom"])
        print("prix : ", p["prix"])
        print("image : ", p["image_source"])
        print("note : ", p["note"])
        print("-" * 70)


def menu():
    while True:
        print()
        print("=" * 40)
        print("          MENU PRINCIPAL")
        print("=" * 40)
        print("1. Lancer le scraping")
        print("2. Afficher les produits")
        print("3. Rechercher un produit")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix in ["0", "1", "2", "3"]:
            return choix
        print("Choix invalide, réessayez.")