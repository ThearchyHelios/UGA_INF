import initialisation
import gestion_de_la_partie
import score_stock

nombre_de_personne = int(input("Il y a combien de joueurs?"))

liste_joueurs = initialisation.initJoueurs(nombre_de_personne)
scores = initialisation.premierTour(liste_joueurs)

while True:
    liste_pioche = initialisation.initPioche(nombre_de_personne)
    gestion_de_la_partie.tourComplet(scores, liste_pioche)
    score_stock.history_save_to_txt("INF101/TP/Projet Final/history.txt", scores)
    # continuer = input("Est-ce que vous voulais rejouer? y ou n")
    # if continuer == "n":
    #     dict_point = {}
    #     for nom in scores:
    #         dict_point[nom] = scores[nom]["point"]
    #     print(dict_point)
    #     exit()
    # else:
    #     # scores = gestion_de_la_partie.rejouer(scores)
    #     dict_point = {}
    #     for nom in scores:
    #         dict_point[nom] = scores[nom]["point"]
    #     print(dict_point)
    #     scores = initialisation.premierTour(liste_joueurs)
    #     for nom in scores:
    #         scores[nom]["point"] = dict_point[nom]
    dict_point = {}
    for nom in scores:
        dict_point[nom] = scores[nom]["point"]
    print(dict_point)
    scores = initialisation.premierTour(liste_joueurs)
    for nom in scores:
        scores[nom]["point"] = dict_point[nom]

# gestion_de_la_partie.bot_decision("history.txt", scores, "a")
