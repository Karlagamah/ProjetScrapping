import csv
import os
import sqlite3

DB_PATH = "data/produits.db"


# ---------------------- CSV ----------------------

def sauvegarder_csv(liste):
    os.makedirs("data", exist_ok=True)

    with open("data/produits.csv", "w", newline="", encoding="utf-8-sig") as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow(["nom", "prix", "image_source", "note"])
        for p in liste:
            ecrivain.writerow([p["nom"], p["prix"], p["image_source"], p["note"]])

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


# ---------------------- SQLite ----------------------

def creer_table():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prix TEXT,
            image_source TEXT,
            note TEXT,
            UNIQUE(nom, prix)
        )"""
    )
    conn.commit()
    conn.close()


def sauvegarder_sqlite(liste):
    creer_table()
    conn = sqlite3.connect(DB_PATH)
    for p in liste:
        conn.execute(
            "INSERT OR IGNORE INTO produits (nom, prix, image_source, note) VALUES (?, ?, ?, ?)",
            (p["nom"], p["prix"], p["image_source"], p["note"]),
        )
    conn.commit()
    conn.close()
    print(len(liste), "produits sauvegardés dans", DB_PATH)


def charger_sqlite():
    creer_table()
    conn = sqlite3.connect(DB_PATH)
    lignes = conn.execute("SELECT nom, prix, image_source, note FROM produits").fetchall()
    conn.close()

    produits = []
    for nom, prix, image_source, note in lignes:
        produits.append({"nom": nom, "prix": prix, "image_source": image_source, "note": note})
    return produits


def rechercher_sqlite(mot):
    creer_table()
    conn = sqlite3.connect(DB_PATH)
    lignes = conn.execute(
        "SELECT nom, prix, image_source, note FROM produits WHERE nom LIKE ?",
        ("%" + mot + "%",),
    ).fetchall()
    conn.close()

    produits = []
    for nom, prix, image_source, note in lignes:
        produits.append({"nom": nom, "prix": prix, "image_source": image_source, "note": note})
    return produits