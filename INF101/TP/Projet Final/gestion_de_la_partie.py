from operator import truediv
import random
import time
import distutils.core

import initialisation


# import keras
# from keras import datasets


def continuer():
    continuer_le_jeux = input("Est-ce que vous voulais continuer? y ou n")
    if continuer_le_jeux == "y":
        return True
    else:
        return False

    # if history["score"][""]


# TODO: 全部将荷答应有关的代码禁用，为了测试
def tourJoueur(j, scores, pioche, score_croupier_premier_round):
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
            print("There are %s players, they have %s " %
                  (len(liste_score), liste_score[i]), end="")
        elif i == len(liste_score) - 1:
            print("%s points." % liste_score[i])
        else:
            print("%s " % liste_score[i], end="")
    print("Le croupier a %s." % score_croupier_premier_round)

    scores[j]["history"]["round %s" % round] = score
    if score == 21:
        print("You win the game!")
        scores[j]["success"] = True
        scores[j]["point"] += 1
        return
    print("You have %s scores now " % score)
    print(scores)
    if bot_decision("INF101/TP/Projet Final/database.txt", scores, j, score_croupier_premier_round):
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
    #
    # time.sleep(2)


def tourComplet(scores, pioche):
    score_croupier_premier_round = croupier_prendre_carte(pioche, 1)
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
            # cest a dire que tous les joueurs sont give up , va gagner les personnes qui gangent le plus score.
            score_croupier = score_croupier_premier_round
            # TODO: Croupier condition
            # while True:
            #     score = croupier_prendre_carte(pioche, 1)
            #     print("Croupier a prendre %s" % score)
            #     score_croupier += score

            nom, score = initialisation.gagnant(scores, random.randint(16, 21))
            for nom_gagner_plus_point in nom:
                for nom_dans_liste in scores:
                    if nom_dans_liste == nom_gagner_plus_point:
                        scores[nom_gagner_plus_point]["success"] = True
                        scores[nom_gagner_plus_point]["point"] += 1
                        print("You have success %s" % nom_gagner_plus_point)
            return
        elif count_out == len(scores):
            # Cest a dire que tous les personnes sont out
            return
        else:
            for nom in scores:
                if not scores[nom]["give_up"] and not scores[nom]["success"] and not scores[nom]["out"] and not \
                        scores[nom][
                            "draw"]:
                    tourJoueur(nom, scores, pioche,
                               score_croupier_premier_round)


def croupier_prendre_carte(pioche, nombre):
    liste_pioche = pioche
    liste_carte = initialisation.piocheCarte(liste_pioche, nombre)
    score = 0
    for carte in liste_carte:
        print("You get %s" % carte)
        score += initialisation.valeurCarte(carte)
    return score


def bot_decision(path, scores, nom, score_croupier_premier_round):
    history = {}
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
        history[count]["success"] = bool(
            distutils.util.strtobool(item_list[-3]))
        history[count]["out"] = bool(distutils.util.strtobool(item_list[-2]))
        history[count]["give_up"] = bool(
            distutils.util.strtobool(item_list[-1]))
        count += 1
    # print(history)
    # new_dict = {}
    # count = 0
    # for key, items in history.items():
    #     if int(history[key]["round"]) != 1:
    #         new_dict[count] = items
    #         count += 1

    score = scores[nom]["score"]
    liste_chance = []

    if score < 12:
        return True
    else:
        success_rate_list = []
        success_list = []
        defayant_list = []
        for i in range(1, 21 - score + 1):
            if i > 10:
                i = 1
            success_list.append(0)
            defayant_list.append(0)

            carte = score + i
            for item in history:
                list_temp_2 = []
                for j in range(int(history[item]["round"]) - 1):
                    list_temp_1 = []

                    for key, item_score in history[item]["score"].items():
                        list_temp_1.append(int(item_score))

                    list_temp_2.append([list_temp_1[j], list_temp_1[j + 1]])
                for k in range(len(list_temp_2)):
                    if list_temp_2[k][0] == carte:
                        if list_temp_2[k][1] > 21:
                            out = True
                        else:
                            out = False

                        feature_liste = [
                            int(list_temp_2[k][0]), out, history[item]["success"]]
                        if feature_liste[1]:
                            defayant_list[i-1] += 1
                        else:
                            success_list[i-1] += 1
        for i in range(len(success_list)):
            success_rate_list.append(success_list[i]/(success_list[i]+ defayant_list[i] + 1))

    success_rate_final = 0
    for j in range(len(success_rate_list)):
        poid = 1 / (2 * (j + 1))
        success_rate_final += success_rate_list[j] * poid
    print("Success rate: %s" % success_rate_final)
    time.sleep(0.01)
    if success_rate_final >= 0.15:
        return True
    else:
        return False

        # if chance_moyenne >= 50:
        #     return True
        # else:
        #     return False

# def croupier_decision(scores, ):
