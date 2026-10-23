

import csv
import os


def sauvegarder_csv(liste):
    os.makedirs("data", exist_ok=True)  

  
    with open("data/produits.csv", "w", newline="", encoding="utf-8-sig") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["nom", "prix", "image_source", "note", "livraison"]) 
        for p in liste:
            ecrivain.writerow([p["nom"], p["prix"], p["image_source"], p["note"], p["livraison"]])

    print(len(liste), "produits sauvegardés dans data/produits.csv")


def charger_csv():
    produits = []
    if not os.path.exists("data/produits.csv"):   
        return produits

    with open("data/produits.csv", "r", encoding="utf-8-sig") as fichier:
        lecteur = csv.DictReader(fichier)  
        for ligne in lecteur:
            ligne["image"] = None   
            produits.append(ligne)
    return produits


def rechercher_produit(liste, mot):
    mot = mot.lower()
    resultat = []
    for p in liste:
        if mot in p["nom"].lower():
            resultat.append(p)
    return resultat
