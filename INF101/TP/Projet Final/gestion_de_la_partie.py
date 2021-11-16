import time

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

    if score == 21:
        print("You win the game!")
        scores[j]["success"] = True
        scores[j]["point"] += 1
        return

    print("You have %s scores now " % score)
    if continuer():
        # if not scores[j]["out"] and not scores[j]["give_up"]
        liste_pioche_joueur = pioche[numero_joueur]
        liste_carte = initialisation.piocheCarte(liste_pioche_joueur, 1)
        for carte in liste_carte:
            print("You get %s" % carte)
            score += initialisation.valeurCarte(carte)
        print("score: %s" % score)
        scores[j]["score"] = score
        if score > 21:
            print("You lose the game!")
            scores[j]["out"] = True
        elif score == 21:
            print("You win the game!")
            scores[j]["success"] = True
            scores[j]["point"] += 1
        print(scores)
    else:
        scores[j]["give_up"] = True
        print("You have given up")

    time.sleep(2)


def tourComplet(scores, pioche):
    while True:
        count_out = 0
        count_giveup = 0
        count_success = 0
        for nom in scores:
            if scores[nom]["out"]:
                count_out += 1
            elif scores[nom]["give_up"]:
                count_giveup += 1
            elif scores[nom]["success"]:
                count_success += 1
            elif not scores[nom]["give_up"] and not scores[nom]["success"]:
                if count_out == len(scores) - 1:  # 只剩一名玩家
                    scores[nom]["success"] = True
                    scores[nom]["point"] += 1
                    print("%s a reussi" % nom)
                else:
                    tourJoueur(nom, scores, pioche)
            else:
                print("Player %s please wait until all players given up" % nom)
        if count_giveup == len(scores) - count_out - count_success:
            if count_success == len(scores) - 1:
                for nom in scores:
                    if scores[nom]["success"] == False:
                        print("You have loss %s" % nom)
                        return
            else:
                nom, score = initialisation.gagnant(scores)
                for nom_gagner_plus_point in nom:
                    for nom_dans_liste in scores:
                        if nom_dans_liste == nom_gagner_plus_point:
                            scores[nom_gagner_plus_point]["success"] = True
                            scores[nom_gagner_plus_point]["point"] += 1
                            print("You have success %s" % nom_gagner_plus_point)

                return
