def extraire_produits(soup):
    produits = soup.select('div[data-cy="title-recipe"]')
    print("le nombre de produits sur la page est : ", len(produits))
    liste = []

    for bloc in produits:
        h2 = bloc.select_one("h2")
        nom = h2.get_text(strip=True) if h2 else "Nom non trouvé"

        carte = bloc.parent
        while carte is not None and carte.name != "[document]" and carte.find("div", class_="a-section aok-relative s-image-square-aspect") is None:
            carte = carte.parent
        if carte is not None and carte.name != "[document]":
            bloc = carte

        bloc_prix = bloc.find("span", class_="a-price")
        prix_tag = bloc_prix.find("span", class_="a-offscreen") if bloc_prix else None
        prix = prix_tag.get_text(strip=True) if prix_tag else "Prix non trouvé"

        img = bloc.select_one("img.s-image")
        image_source = img.get("src") if img else "Image non trouvée"

        note_article = bloc.find("div", class_="a-row a-size-small")
        note = note_article.get_text(" ", strip=True) if note_article else "Note non trouvée"

        liste.append({
            "nom": nom,
            "prix": prix,
            "image_source": image_source,
            "note": note,
        })

    return liste