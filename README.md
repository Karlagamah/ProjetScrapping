# Amazon Scraper

Projet de cours : récupération d'informations sur des produits Amazon (nom, prix, image, note, livraison) avec **Selenium** et **BeautifulSoup**, organisé selon l'architecture **MVC**.

## Fonctionnalités

- Ouvre une page catégorie d'amazon.fr dans Chrome (Selenium) et fait défiler la page pour charger les articles.
- Extrait pour chaque produit : le nom, le prix, le lien de l'image, la note et la livraison (BeautifulSoup).
- Affiche les produits dans la console.
- Propose un menu principal en console.
- Sauvegarde et exporte les produits dans des fichiers CSV.





## Lancement




Le programme scrape la page, affiche les produits, puis affiche le menu principal.

## Architecture


amazon_scraper/
├── main.py                  Point d'entrée du programme
├── config.py                Adresses (URL) des pages à scraper
├── requirements.txt         Bibliothèques à installer
├── README.md                Présentation du projet
├── data/                    Fichier CSV de sauvegarde des produits (produits.csv)
└── app/
    ├── controllers/
    │   └── scraping_controller.py   Enchaîne le scraping, l'extraction et l'affichage
    ├── models/
    │   ├── produit.py               Modèle d'un produit
    │   └── depot.py                 Sauvegarde et lecture des produits (CSV dans data/)
    ├── scraper/
    │   ├── driver.py                Création du navigateur Chrome
    │   ├── amazon_scraper.py        Chargement de la page, défilement, récupération du HTML
    │   └── parsing.py               Extraction des informations de chaque produit
    └── views/
        ├── console_view.py          Affichage des produits et menu principal
        └── export_view.py           Export des résultats en CSV




