# Amazon Scraper

Projet de cours : récupération d'informations sur des produits Amazon (nom, prix, image, note, livraison) avec **Selenium** et **BeautifulSoup**, organisé selon l'architecture **MVC**.

## Fonctionnalités

- Ouvre une page catégorie d'amazon.fr dans Chrome (Selenium) et fait défiler la page pour charger les articles.
- Extrait pour chaque produit : le nom, le prix, le lien de l'image, la note et la livraison (BeautifulSoup).
- Affiche les produits dans la console.
- Propose un menu principal en console.
- Sauvegarde et exporte les produits dans des fichiers CSV.

## Prérequis

- Python 3
- Google Chrome installé (Selenium télécharge automatiquement le pilote adapté)

## Installation

```
py -m pip install -r requirements.txt
```

## Lancement

Depuis la racine du projet, dans le terminal :

```
py main.py
```

Le programme scrape la page, affiche les produits, puis affiche le menu principal.

## Configuration

Les adresses des pages à scraper sont dans `config.py` (`URL` et `URL_2`). Pour scraper la deuxième page, décommenter la ligne `lancer(URL_2)` dans `main.py`.

## Architecture

```
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
```

## État d'avancement

- Le menu renvoie le choix de l'utilisateur ; les options 2, 3 et 4 ne sont pas encore reliées aux fonctions de `depot.py` et `export_view.py`.
- `produit.py` est à compléter.
- Les sélecteurs CSS dépendent du HTML d'Amazon, qui change régulièrement : ils peuvent devoir être mis à jour.

## Avertissement

Projet réalisé dans un but pédagogique. Le scraping automatisé est contraire aux conditions d'utilisation d'Amazon : à utiliser avec modération et sans usage commercial.

## Auteurs

À compléter : nom(s), cours, date.
