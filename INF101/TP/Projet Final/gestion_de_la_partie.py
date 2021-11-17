import time

import initialisation


def continuer(path, score):
    history = {}
    scores = []
    count = 0
    for line in open(path, "r"):
        line = line[:-1]  # delete \n
        # list_chaque_personne = f.split("\n")
        history[count] = {}
        item_list = line.split(",")
        history[count]["round"] = int(item_list[0])
        history[count]["score"] = {}
        for score in item_list[1:-3]:
            list_temp = score.split(":")
            history[count]["score"][list_temp[0]] = int(list_temp[1])
        history[count]["success"] = bool(item_list[-3])
        history[count]["out"] = bool(item_list[-2])
        history[count]["give_up"] = bool(item_list[-1])
        count += 1
    print(history)
    continuer_le_jeux = input("Est-ce que vous voulais continuer? y ou n")
    if continuer_le_jeux == "y":
        return True
    else:
        return False

    # if history["score"][""]


def tourJoueur(j, scores, pioche):
    score = 0
    round = 0
    print(scores)
    liste_score = []
    for nom in scores:
        if nom == j:
            for nom_item, item in scores[nom].items():
                if nom_item == "score":
                    score = item
                if nom_item == "round":
                    round = item
        for nom_item, item in scores[nom].items():
            if nom_item == "score":
                liste_score.append(item)

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

    scores[j]["history"]["round %s" % round] = score
    if score == 21:
        print("You win the game!")
        scores[j]["success"] = True
        scores[j]["point"] += 1
        return
    print("You have %s scores now " % score)
    print(scores)
    if continuer("history.txt", scores):
        # if not scores[j]["out"] and not scores[j]["give_up"]

        liste_pioche = pioche
        liste_carte = initialisation.piocheCarte(liste_pioche, 1)
        for carte in liste_carte:
            print("You get %s" % carte)
            score += initialisation.valeurCarte(carte)
        print("score: %s" % score)
        scores[j]["score"] = score
        if score > 21:
            print("You lose the game!")
            scores[j]["out"] = True
            scores[j]["history"]["round %s" % (round + 1)] = score
        elif score == 21:
            print("You win the game!")
            scores[j]["success"] = True
            scores[j]["point"] += 1
            scores[j]["history"]["round %s" % (round + 1)] = score
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

        if count_giveup == len(scores) - count_out - count_success:
            if count_success == len(scores) - 1:  # il est le seul person de n'a pas reussir
                for nom in scores:
                    if scores[nom]["success"] == False:
                        print("You have loss %s" % nom)
                        return
            elif count_out == len(scores) - 1:  # il est le seule personne n'a pas out donc il est reussir
                for nom in scores:
                    if scores[nom]["out"] == False:  # pour trouver le personne
                        print("You win the game! %s" % nom)
                        scores[nom]["success"] = True
                        scores[nom]["point"] += 1
                        return
            else:  # cest a dire que tous les joueurs sont give up , va gagner les personnes qui gangent le plus score.
                nom, score = initialisation.gagnant(scores)
                for nom_gagner_plus_point in nom:
                    for nom_dans_liste in scores:
                        if nom_dans_liste == nom_gagner_plus_point:
                            scores[nom_gagner_plus_point]["success"] = True
                            scores[nom_gagner_plus_point]["point"] += 1
                            print("You have success %s" % nom_gagner_plus_point)
                return

        for nom in scores:
            if not scores[nom]["give_up"] and not scores[nom]["success"] and not scores[nom]["out"]:
                tourJoueur(nom, scores, pioche)
