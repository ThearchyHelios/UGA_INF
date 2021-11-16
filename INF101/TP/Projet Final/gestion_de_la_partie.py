import initialisation


def continuer():
    continuer_le_jeux = input("Est-ce que vous voulais continuer? y ou n")
    if continuer_le_jeux == "y":
        return True
    else:
        return False


def tourJoueur(j, scores, pioche):
    score = 0
    round = 0
    print(scores)
    liste_score = []
    count_joueurs = 0
    numero_joueur = 0
    for nom in scores:
        if nom == j:
            numero_joueur = count_joueurs
            for nom_item, item in scores[nom].items():
                if nom_item == "score":
                    score = item
                if nom_item == "round":
                    round = item
        for nom_item, item in scores[nom].items():
            if nom_item == "score":
                liste_score.append(item)
        count_joueurs += 1

    round += 1
    scores[j]["round"] = round
    print("--------------------")
    print("The %s round " % round)
    print("Name of the player: %s" % j)
    for i in range(len(liste_score)):
        if i == 0:
            print("There are %s players, they have %s " % (len(liste_score), liste_score[i]), end="")
        elif i == len(liste_score) - 1:
            print("%s points." % liste_score[i])
        else:
            print("%s " % liste_score[i], end="")

    print("You have %s scores now " % score)
    if continuer():
        liste_pioche_joueur = pioche[numero_joueur]
        liste_carte = initialisation.piocheCarte(liste_pioche_joueur, 1)
        for carte in liste_carte:
            print("You get %s" % carte)
            score += initialisation.valeurCarte(carte)
        print("score: %s" % score)
        scores[j]["score"] = score
        if score > 21:
            print("You lose the game!")
            del scores[j]
        print(scores)
    else:
        print("You have been deleted from list")


