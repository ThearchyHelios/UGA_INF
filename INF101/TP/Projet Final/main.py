import initialisation
import gestion_de_la_partie
import score_stock

nombre_de_personne = int(input("Il y a combien de joueurs?"))

liste_joueurs = initialisation.initJoueurs(nombre_de_personne)
scores = initialisation.premierTour(liste_joueurs)

while True:
    liste_pioche_chaque_personne = initialisation.initPioche(nombre_de_personne)
    gestion_de_la_partie.tourComplet(scores, liste_pioche_chaque_personne)
    score_stock.history_save_to_txt("history.txt", scores)
    continuer = input("Est-ce que vous voulais rejouer? y ou n")
    if continuer == "n":
        dict_point = {}
        for nom in scores:
            dict_point[nom] = scores[nom]["point"]
        print(dict_point)
        break
    else:
        # scores = gestion_de_la_partie.rejouer(scores)
        dict_point = {}
        for nom in scores:
            dict_point[nom] = scores[nom]["point"]
        print(dict_point)
        scores = initialisation.premierTour(liste_joueurs)
        for nom in scores:
            scores[nom]["point"] = dict_point[nom]
