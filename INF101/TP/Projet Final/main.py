from operator import truediv
import random
import time
import distutils.core
import matplotlib.pyplot as plt
import os.path
from pandas import period_range
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from time import perf_counter


def history_save_to_txt(path, scores):
    # liste_histoire = {}
    # for nom in scores:
    #     for key, items in scores[nom]["history"].items():
    #         liste_histoire[nom][key] = items
    for nom in scores:
        count_round = len(scores[nom]["history"])
        success = False
        out = False
        give_up = False
        history = ""
        if count_round == 1:
            continue
        for items in scores[nom]:
            if scores[nom]["success"]:
                success = True
            if scores[nom]["out"]:
                out = True
            if scores[nom]["give_up"]:
                give_up = True
        for key, items in scores[nom]["history"].items():
            history = history + str(key) + ":" + str(items) + ","

        string = str(count_round) + "," + history + str(success) + "," + str(
            out) + "," + str(give_up) + "\n"
        with open(path, 'a+') as f:
            f.write(string)
            f.close()


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
        nombre = 0
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


def piocheCarte(x):
    global liste_pioche
    liste_carte = []
    for i in range(x):
        liste_carte.append(liste_pioche[i])
        del liste_pioche[0]

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
            "mise": 1000,
            "mise_round": 0,
            "history": {}
        }
    return dict_joueurs


def premierTour(scores):
    global liste_pioche

    liste_carte_joueurs = []
    for i in range(len(scores)):
        if len(liste_pioche) <= 2:
            liste_pioche = initPioche(len(scores))
        valeur_premier_round = piocheCarte(2)
        liste_carte_joueurs.append(valeur_premier_round)

    count = 0
    for nom in scores:
        liste_carte_joueur = liste_carte_joueurs[count]
        for carte in liste_carte_joueur:
            temp = int(valeurCarte(carte))
            if temp == 0:
                if scores[nom]["score"] == 0:
                    print("Cest ton premier tour!")
                else:
                    print("T'as %s maintenant." % scores[nom]["score"])
                nombre = int(
                    input("Cest A: Quel valeur vous voulais choisi? 1 ou 11?"))
                if nombre == 1:
                    temp = 1
                elif nombre == 11:
                    temp = 11
                else:
                    temp = 1
            scores[nom]["score"] += temp
        count += 1
    return scores


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
                mise_round = scores[nom]["mise_round"]
                scores[nom]["mise"] += mise_round
                scores[nom]["draw"] = True
            else:
                print("You have loss the game! %s" % nom)

    for nom in scores:
        if scores[nom]["score"] == point_gagnant_plus:
            nom_gagnant_plus.append(nom)
    # print(scores)
    return nom_gagnant_plus, point_gagnant_plus


def continuer():
    continuer_le_jeux = input("Est-ce que vous voulais continuer? y ou n")
    if continuer_le_jeux == "y":
        return True
    else:
        return False

    # if history["score"][""]


# TODO: 全部将荷答应有关的代码禁用，为了测试
def tourJoueur(j, scores, score_croupier_premier_round):
    global liste_pioche
    score = 0
    round = 0
    # print(scores)
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
                  (len(liste_score), liste_score[i]),
                  end="")
        elif i == len(liste_score) - 1:
            print("%s points." % liste_score[i])
        else:
            print("%s " % liste_score[i], end="")
    print("Le croupier a %s." % score_croupier_premier_round)

    scores[j]["history"]["round %s" % round] = score
    print("You have %s scores now " % score)
    # print(scores)
    # data_folder = os.path.join("INF101", "TP", "Projet Final")
    # file = os.path.join(data_folder, "database.txt")

    # for nom in scores:
    #     if round == 1 and scores[nom]["score"] == 21:
    #         print("Black Jack!")
    #         scores[nom]["success"] = True
    #         mise_round = scores[nom]["mise_round"]
    #         scores[nom]["mise"] += mise_round * 2.5

    # if bot_decision("INF101/TP/Projet Final/database.txt", scores, j,
    #                 score_croupier_premier_round):
    if continuer():
        if liste_pioche == []:
            liste_pioche = initPioche(len(scores))
        liste_carte = piocheCarte(1)
        for carte in liste_carte:
            print("You get %s" % carte)
            temp = int(valeurCarte(carte))
            if temp == 0:
                nombre = int(
                    input("Cest A: Quel valeur vous voulais choisi? 1 ou 11?"))
                if nombre == 1:
                    temp = 1
                elif nombre == 11:
                    temp = 11
                else:
                    temp = 1
            score += temp
        print("score: %s" % score)
        scores[j]["score"] = score
        if score > 21:
            print("You lose the game!")
            scores[j]["out"] = True
            scores[j]["history"]["round %s" % (round + 1)] = score

        # elif score == 21:
        #     print("You win the game!")
        #     scores[j]["success"] = True
        #     scores[j]["point"] += 1
        #     scores[j]["history"]["round %s" % (round + 1)] = score
    else:
        scores[j]["give_up"] = True
        print("You have given up")
    #
    # time.sleep(2)


def tourComplet(scores):
    global liste_pioche
    if liste_pioche == []:
        liste_pioche = initPioche(len(scores))
    score_croupier_premier_round = croupier_prendre_carte(1)
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

            valeur_croupier = random.randint(16, 21)
            print("Croupier have %s " % valeur_croupier)
            nom, score = gagnant(scores, valeur_croupier)
            for nom_gagner_plus_point in nom:
                for nom in scores:
                    if nom == nom_gagner_plus_point:
                        scores[nom_gagner_plus_point]["success"] = True
                        scores[nom_gagner_plus_point]["point"] += 1
                        mise_round = scores[nom_gagner_plus_point][
                            "mise_round"]
                        scores[nom_gagner_plus_point]["mise"] += mise_round * 2
                        print("You have success %s" % nom_gagner_plus_point)
            return
        elif count_out == len(scores):
            # Cest a dire que tous les personnes sont out
            print("Croupier win")
            return
        else:
            for nom in scores:
                if not scores[nom]["give_up"] and not scores[nom]["success"] and not scores[nom]["out"] and not \
                        scores[nom]["draw"] and scores[nom]["score"] != 21:
                    tourJoueur(nom, scores, score_croupier_premier_round)


def croupier_prendre_carte(nombre):
    global liste_pioche
    if liste_pioche == []:
        liste_pioche = initPioche(len(scores))
    liste_carte = piocheCarte(nombre)
    score = 0
    for carte in liste_carte:
        print("You get %s" % carte)
        score += valeurCarte(carte)
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
        length = 21 - score - 1
        # win_rate = pg.plot()
        # win_rate.setWindowTitle('Win Rate Bar Graph')
        # x = np.arange(length)
        # x = x + score + 1

        success_rate_list = []
        success_list = []
        defayant_list = []
        for i in range(1, 21 - score):
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
                            int(list_temp_2[k][0]), out,
                            history[item]["success"]
                        ]
                        if feature_liste[1]:
                            defayant_list[i - 1] += 1
                        else:
                            success_list[i - 1] += 1
        for i in range(len(success_list)):
            success_rate_list.append(success_list[i] /
                                     (success_list[i] + defayant_list[i] + 1))

    # win_rate.plot(x=x,
    #               y=success_rate_list,
    #               symbolBrush=(255, 0, 0),
    #               symbolPen='w')

    success_rate_final = 0
    for j in range(len(success_rate_list)):
        poid = 1 / (2 * (j + 1))
        success_rate_final += success_rate_list[j] * poid
    print("Success rate: %s" % success_rate_final)
    # time.sleep(0.01)
    # pg.exec()

    if success_rate_final >= 0.2:
        return True
    else:
        return False


nombre_de_personne = int(input("Il y a combien de joueurs?"))

liste_joueurs = initJoueurs(nombre_de_personne)
liste_pioche = initPioche(nombre_de_personne)
scores = initScores(liste_joueurs, 0)

while True:
    liste_joueurs = []
    for nom in scores:
        liste_joueurs.append(nom)
    dict_point = {}
    dict_mise = {}
    for nom in scores:
        dict_point[nom] = scores[nom]["point"]
        dict_mise[nom] = scores[nom]["mise"]
    print(dict_point)
    print(dict_mise)
    input("Press Enter to continue...")
    scores = initScores(liste_joueurs, 0)
    for nom in scores:
        scores[nom]["point"] = dict_point[nom]
        scores[nom]["mise"] = dict_mise[nom]

    for nom in list(scores.keys()):
        if scores[nom]["mise"] <= 0:
            scores.pop(nom)
            print("%s is out" % nom)
    
    if len(scores) == 1:
        print("%s win" % list(scores.keys())[0])
        break
    
    for nom in scores:
        mise_round = int(input("%s, misez combien?" % nom))
        while mise_round > scores[nom]["mise"]:
            mise_round = int(
                input("Il faut inerieur a ton mise!\n%s, misez combien?" %
                      nom))
        scores[nom]["mise_round"] = mise_round
        scores[nom]["mise"] -= mise_round
    scores = premierTour(scores)
    for nom in scores:
        if scores[nom]["score"] == 21:
            scores[nom]["success"] = True
            
            scores[nom]["point"] += 1
            scores[nom]["mise"] += (scores[nom]["mise_round"]) * 2.5
    print(len(liste_pioche))
    tourComplet(scores)
    history_save_to_txt("INF101/TP/Projet Final/history.txt", scores)
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

# gestion_de_la_partie.bot_decision("history.txt", scores, "a")
