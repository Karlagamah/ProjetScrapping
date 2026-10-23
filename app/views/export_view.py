

import csv
import os


def exporter_csv(liste):
    os.makedirs("exports", exist_ok=True)   # crée le dossier exports s'il n'existe pas

    with open("exports/produits.csv", "w", newline="", encoding="utf-8-sig") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["nom", "prix", "image_source", "note", "livraison"])   # ligne des titres
        for p in liste:
            ecrivain.writerow([p["nom"], p["prix"], p["image_source"], p["note"], p["livraison"]])

    print(len(liste), "produits exportés dans exports/produits.csv")
