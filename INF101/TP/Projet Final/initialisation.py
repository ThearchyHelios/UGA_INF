import random


def paquet():
    liste_carte = []
    #     Ajouter des cartes carreau dans la liste
    for i in range(1, 14):
        if i == 1:
            i = "A"
        elif i == 11:
            i = "valet"
        elif i == 12:
            i = "dame"
        elif i == 13:
            i = "roi"
        temp = str(i) + " de carreau"
        liste_carte.append(temp)

    #     Ajouter des cartes pique dans la liste
    for i in range(1, 14):
        if i == 1:
            i = "A"
        elif i == 11:
            i = "valet"
        elif i == 12:
            i = "dame"
        elif i == 13:
            i = "roi"
        temp = str(i) + " de pique"
        liste_carte.append(temp)

    #     Ajouter des cartes trefle dans la liste
    for i in range(1, 14):
        if i == 1:
            i = "A"
        elif i == 11:
            i = "valet"
        elif i == 12:
            i = "dame"
        elif i == 13:
            i = "roi"
        temp = str(i) + " de trefle"
        liste_carte.append(temp)

    #     Ajouter des cartes coeur dans la liste
    for i in range(1, 14):
        if i == 1:
            i = "A"
        elif i == 11:
            i = "valet"
        elif i == 12:
            i = "dame"
        elif i == 13:
            i = "roi"
        temp = str(i) + " de coeur"
        liste_carte.append(temp)

    liste_ramplacer = []
    for i in range(len(liste_carte)):
        temp_random = random.randint(0, len(liste_carte) - 1)
        temp = liste_carte[i]
        liste_carte[i] = liste_carte[temp_random]
        liste_carte[temp_random] = temp
        liste_ramplacer.append(i)
        liste_ramplacer.append(temp_random)
    return liste_carte


def valeurCarte(carte):
    temp = str(carte)
    nombre_liste = temp.split(" ")
    if nombre_liste[0] == "A":
        # nombre = int(input("Cest A: Quel valeur vous voulais choisi? 1 ou 11?"))
        nombre = 1
    elif nombre_liste[0] == "valet" or nombre_liste[
            0] == "dame" or nombre_liste[0] == "roi":
        nombre = 10
    else:
        nombre = int(nombre_liste[0])
    return nombre


def initPioche(n):
    liste_carte_remplacer = []
    for i in range(n):
        liste_paquet = paquet()
        for j in liste_paquet:
            liste_carte_remplacer.append(j)
    return liste_carte_remplacer


# TODO: bug


def piocheCarte(p, x):
    liste_carte = []
    for i in range(x):
        liste_carte.append(p[i])
        p.append(p[i])
        del p[0]

    return liste_carte


def initJoueurs(n):
    liste_joueurs = []
    for i in range(n):
        nom = input("Quel est le nom du joueur?")
        liste_joueurs.append(nom)
    return liste_joueurs


def initScores(joueurs, v):
    dict_joueurs = {}
    for nom in joueurs:
        dict_joueurs[nom] = {
            "score": v,
            "round": 0,
            "give_up": False,
            "out": False,
            "success": False,
            "draw": False,
            "point": 0,
            "mise": [],
            "history": {}
        }
    return dict_joueurs


def premierTour(joueurs):
    liste_carte_joueurs = []
    dict_joueurs = initScores(joueurs, 0)
    for i in range(len(joueurs)):
        liste_carte_joueurs.append(piocheCarte(initPioche(len(joueurs)), 2))
    count = 0

    for liste_carte_joueur in liste_carte_joueurs:
        for carte in liste_carte_joueur:
            dict_joueurs[joueurs[count]]["score"] += int(valeurCarte(carte))
        count += 1
    return dict_joueurs


# TODO: changer le fonction pour ajouter un Croupier et comparer les scores avec Croupier
def gagnant(scores, valeur_croupier):
    # list_score = []
    nom_gagnant_plus = []
    point_gagnant_plus = 0
    for nom in scores:
        score = scores[nom]["score"]
        if scores[nom]["give_up"] == True and scores[nom][
                "out"] == False and scores[nom]["success"] == False:
            if score > valeur_croupier:
                point_gagnant_plus = score  # reussir, parce que le score est > que Croupier
            elif score == valeur_croupier:
                print("add points here")
                scores[nom]["draw"] = True
                # TODO: add point here
            else:
                print("You have loss the game! %s" % nom)

    for nom in scores:
        if scores[nom]["score"] == point_gagnant_plus:
            nom_gagnant_plus.append(nom)
    print(scores)
    return nom_gagnant_plus, point_gagnant_plus
