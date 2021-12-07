'''
Author: JIANG Yilun
Date: 2021-11-28 20:44:31
LastEditTime: 2021-12-07 15:47:53
LastEditors: JIANG Yilun
Description: 
FilePath: /UGA_INF/INF101/TP/Projet Final/main.py
'''
import sys
from operator import truediv
import random
from sqlite3 import paramstyle
from sre_constants import SUCCESS
import time
import distutils.core
import os.path
import multiprocessing as mp
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QDialogButtonBox
from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget
import pyqtgraph as pg
import numpy as np



def history_save_to_txt(path, data):
    """ Cette fonction permet de sauvegarder l'historique dans un fichier txt.

    Args:
        path (str): Fichiers TXT correspondants
        data (dict): Donnees à déposer dans le fichier
    """
    count_round = len(data["history"])
    success = False
    out = False
    give_up = False
    draw = False
    history = ""
    croupier_premier_round = str(data["croupier_premier_round"])
    croupier_value_final = str(data["croupier_value_final"])
    if count_round >= 1:
        for items in data:
            if data["success"]:
                success = True
            if data["out"]:
                out = True
            if data["give_up"]:
                give_up = True
            if data["draw"]:
                draw = True
        for key, items in data["history"].items():
            history = history + str(key) + ":" + str(items) + ","

        string = str(
            count_round
        ) + "," + croupier_premier_round + "," + croupier_value_final + "," + history + str(
            success) + "," + str(out) + "," + str(give_up) + "," + str(
                draw) + "\n"
        with open(path, 'a+') as f:
            f.write(string)
            f.close()


def paquet():
    """ Cette fonction est utilisée pour générer un jeu de 52 cartes mélangées.

    Returns:
        list: Une liste avec 52 cartes mélangées
    """
    liste_carte = []
    #     Ajouter des cartes carreau dans la liste
    list_temp = [" de carreau", " de pique", " de trefle", " de coeur"]
    for temp in list_temp:
        for i in range(1, 14):
            if i == 1:
                i = "A"
            elif i == 11:
                i = "valet"
            elif i == 12:
                i = "dame"
            elif i == 13:
                i = "roi"
            mot = str(i) + temp
            liste_carte.append(mot)

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
    """ Cette fonction est utilisée pour obtenir la valeur de la carte

    Args:
        carte (str): Cartes saisies. Ex: "As de carreau"

    Returns:
        int: Retourne la valeur de cette carte. Si la fonction retourne 0, alors la carte d'entrée est un As.
    """
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
    """ Cette fonction est utilisée pour générer une pioche de taille correspondante au nombre de joueurs en jeu.
        Si le nombre de participants est de 3, alors la taille du jeu est de 3*52=156, si le nombre de participants est de 6, alors la taille du jeu est de 6*52=312.

    Args:
        n (int): Nombre de participants au jeu

    Returns:
        list: Nombre de cartes en fonction du nombre de participants
    """
    liste_carte_remplacer = []
    for i in range(n):
        liste_paquet = paquet()
        for j in liste_paquet:
            liste_carte_remplacer.append(j)
    return liste_carte_remplacer


def piocheCarte(liste_pioche, x):
    """ Cette fonction renvoie le nombre x de cartes de la pioche.

    Args:
        x (int): Nombre de cartes à retourner

    Returns:
        list: Cartes retournées avec le nombre x.
    """
    liste_carte = []
    for i in range(x):
        liste_carte.append(liste_pioche[i])
        del liste_pioche[0]

    return liste_carte


def initJoueurs(n):
    """ Cette fonction est utilisée pour demander à l'utilisateur les noms des joueurs et renvoyer une liste avec les noms de chacun d'entre eux.

    Args:
        n (int): Nombre de participants au jeu

    Returns:
        dict: Une liste avec les noms de tous les joueurs.
    """
    liste_joueurs = []
    for i in range(n):
        nom = input("Quel est le nom du joueur?")
        while "Ordi" in nom:
            print("Votre nom ne peu pas contenir le mot 'ordi'.")
            nom = input("Quel est le nom du joueur?")
        liste_joueurs.append(nom)
    return liste_joueurs


def initOrdi(n):
    liste_ordi = []
    for i in range(n):
        liste_ordi.append("Ordi " + str(i + 1))
    return liste_ordi


def initScores(liste_joueurs, liste_ordi, v):
    """ Fonction permettant d'initialiser les informations du joueur, y compris la remise à zéro de son score et de ses différents
    statuts. Renvoie également ["ordi"] = Vrai s'il s'agit d'un joueur informatique, et ["ordi"] = Faux s'il s'agit d'un joueur humain.

    Args:
        liste_joueurs (list): Une liste avec les noms de tous les joueurs humains.
        liste_ordi (list): Une liste avec les noms de tous les joueurs ordinateurs.
        v (int): Attribuer un score spécifique à tous les joueurs (utilisé par défaut au tour 1, où le tour 2 le tour 3 ne s'applique pas, par défaut à 0)
    sokem : args v pas compris

    Returns:
        dict: Retourne le dictionnaire initialisé.
    """

    dict_joueurs = {}
    for nom in liste_joueurs:
        dict_joueurs[nom] = {
            "score": v,
            "round": 0,
            "croupier_premier_round": 0,
            "croupier_value_final": 0,
            "ordi": False,
            "give_up": False,
            "out": False,
            "success": False,
            "draw": False,
            "blackjack": False,
            "point": 0,
            "mise": 1000,
            "mise_round": 0,
            "history": {}
        }
    for nom in liste_ordi:
        dict_joueurs[nom] = {
            "score": v,
            "round": 0,
            "croupier_premier_round": 0,
            "croupier_value_final": 0,
            "ordi": True,
            "give_up": False,
            "out": False,
            "success": False,
            "draw": False,
            "blackjack": False,
            "point": 0,
            "mise": 1000,
            "mise_round": 0,
            "history": {}
        }
    return dict_joueurs


def premierTour(liste_pioche, scores):
    """ Cette fonction est utilisée pour initialiser le score du joueur et permet de tirer deux cartes pour le premier tour.

    Args:
        scores (dict): Scores des joueurs

    Returns:
        dict: Scores des joueurs
    """

    liste_carte_joueurs = []
    for i in range(len(scores)):
        if len(liste_pioche) <= 2:
            liste_pioche = initPioche(len(scores))
        valeur_premier_round = piocheCarte(liste_pioche, 2)
        liste_carte_joueurs.append(valeur_premier_round)

    count = 0
    for nom in scores:
        liste_carte_joueur = liste_carte_joueurs[count]
        for carte in liste_carte_joueur:
            temp = int(valeurCarte(carte))
            if temp == 0:
                if scores[nom]["ordi"] == False:
                    if scores[nom]["score"] == 0:
                        print("Cest ton premier tour!")
                    else:
                        print("Tu as %s maintenant." % scores[nom]["score"])
                    nombre = int(
                        input(
                            "Vous avez obtenu un as! Quel valeur voulez-vous choisir? (1 ou 11)"
                        ))
                    if nombre == 1:
                        temp = 1
                    elif nombre == 11:
                        temp = 11
                    else:
                        temp = 1
                else:
                    temp = 11
            scores[nom]["score"] += temp
        count += 1
    return scores


def gagnant(scores, valeur_croupier):
    """ Cette fonction est utilisée pour comparer les scores de tous les joueurs encore en jeu avec ceux de la banque. Si il y a plus de joueurs vivants que de loteries, alors elle retourne les noms de tous les joueurs vivants.
    sokem : pas compris

    Args:
        scores (dict): Scores des joueurs
        valeur_croupier (int): Valeur du croupier

    Returns:
        list: Liste des noms des joueurs encore en jeu.
    """
    nom_gagnant_plus = []
    point_gagnant_plus = 0
    for nom in scores:
        score = scores[nom]["score"]
        if scores[nom]["give_up"] == True and scores[nom][
                "out"] == False and scores[nom]["success"] == False:
            if score > valeur_croupier:
                point_gagnant_plus = score  # reussir, parce que le score est > que Croupier
                nom_gagnant_plus.append(nom)
            elif score == valeur_croupier:
                print("%s, vous etes à égalité avec le croupier !" % nom)
                mise_round = scores[nom]["mise_round"]
                scores[nom]["mise"] += mise_round
                scores[nom]["draw"] = True
            else:
                print("Vous avez perdu! %s" % nom)

    # print(scores)
    return nom_gagnant_plus, point_gagnant_plus


def joueur_continuer() -> bool:
    """ Cette fonction est utilisée pour demander au joueur s'il veut abandonner.

    Returns:
        bool: Retourne True si le joueur veut abandonner, False sinon.
    """
    continuer_le_jeux = input("Voulez-vous piocher? y ou n ")
    if continuer_le_jeux == "y":
        return True
    else:
        return False


def tourJoueur(liste_pioche, j, scores, score_croupier_premier_round):
    """ Cette fonction lance un nouveau tour de jeu et peut afficher le nombre de tours passés, le scores de tous les joueurs, et celui de ceux encore en jeu.
    sokem : revoir tt la fonction
    Args:
        j (str): Nom du joueur
        scores (dict): Scores des joueurs
        score_croupier_premier_round (int): Score du croupier au premier tour
    """
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
    print("Tour %s" % round)
    print("%s, a vous de jouer." % j)
    for i in range(len(liste_score)):
        if i == 0:
            # sokem probleme avec le print
            print("Il y a %s joueurs qui on %s " %
                  (len(liste_score), liste_score[i]),
                  end="")
        elif i == len(liste_score) - 1:
            print("%s points." % liste_score[i])
        else:
            print("%s " % liste_score[i], end="")
    print("Le croupier a %s points." % score_croupier_premier_round)

    scores[j]["history"]["round %s" % round] = score
    print("Votres score est de %s. " % score)

    if scores[j]["ordi"] == False:
        print("debug")
        if joueur_continuer() == True:
            if liste_pioche == []:
                liste_pioche = initPioche(len(scores))
            liste_carte = piocheCarte(liste_pioche, 1)
            for carte in liste_carte:
                print("Voici la carte que vous avez pioché : %s" % carte)
                temp = int(valeurCarte(carte))
                if temp == 0:
                    if scores[j]["score"] < 12:
                        temp = 11
                    else:
                        temp = 1
                score += temp
            print("Votre score est de %s points." % score)
            scores[j]["score"] = score
            if score > 21:
                print("Vous avez perdu!")
                scores[j]["out"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score
            if score == 21:
                scores[j]["give_up"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score

        else:
            scores[j]["give_up"] = True
            print("Votre tour est términé.")
        time.sleep(2)

    elif scores[j]["ordi"] == True:
        if bot_decision(liste_pioche, scores, j):
            if liste_pioche == []:
                liste_pioche = initPioche(len(scores))
            liste_carte = piocheCarte(liste_pioche, 1)
            for carte in liste_carte:
                print("Voici la carte que vous avez pioché : %s" % carte)
                temp = int(valeurCarte(carte))
                if temp == 0:
                    if scores[j]["score"] < 12:
                        temp = 11
                    else:
                        temp = 1
                score += temp
            print("Votre score est de %s points." % score)
            scores[j]["score"] = score
            if score > 21:
                print("Vous avez perdu!")
                scores[j]["out"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score
            if score == 21:
                scores[j]["give_up"] = True
                scores[j]["history"]["round %s" % (round + 1)] = score

        else:
            scores[j]["give_up"] = True
            print("Votre tour est términé.")

        # time.sleep(2)


def tourComplet(liste_pioche, scores):
    """ Cette méthode comprend l'ensemble du jeu et des règles

    Args:
        liste_pioche (list): Pile de cartes
        scores (dict): Scores des joueurs
    """
    if liste_pioche == []:
        liste_pioche = initPioche(len(scores))
    score_croupier_premier_round = croupier_prendre_carte(liste_pioche, 1)
    if score_croupier_premier_round == 0:
        score_croupier_premier_round = 11
    for nom in scores:
        scores[nom]["croupier_premier_round"] = score_croupier_premier_round
    count_blackjack = 0
    for nom in scores:
        if scores[nom]["blackjack"] == True:
            print("%s Black Jack!" % nom)
            count_blackjack += 1
    if count_blackjack > 0:
        return

    while True:
        count_out = 0
        count_giveup = 0
        count_success = 0
        count_21 = 0
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

            # while True:
            #     score = croupier_prendre_carte(pioche, 1)
            #     print("Croupier a prendre %s" % score)
            #     score_croupier += score

            while score_croupier < 17:
                score = croupier_prendre_carte(liste_pioche, 1)
                print("Le score du croupier est maintenant de %s points." % score)
                score_croupier += score
                mise_round_total = 0
            print("Le croupier a un score de %s points." % score_croupier)
            if score_croupier > 21:
                for nom in scores:
                    if scores[nom]["out"] == False:
                        scores[nom]["success"] = True
                        mise_round = scores[nom]["mise_round"]
                        scores[nom]["mise"] += mise_round
                        scores[nom]["point"] += 1
                    scores[nom]["croupier_value_final"] = score_croupier
                return
            else:
                for nom in scores:
                    mise_round_total += scores[nom]["mise_round"]
                list_pourcentage_mise = []
                for nom in scores:
                    if scores[nom]["out"] == False:
                        list_pourcentage_mise.append(
                            scores[nom]["mise_round"] / (mise_round_total + 1))
                list_pourcentage_mise_total = 0
                for pourcentage in list_pourcentage_mise:
                    list_pourcentage_mise_total += pourcentage
                temp = 21 - score_croupier
                liste_pioche_pourcentage = []
                for i in range(1, temp + 1):
                    count = 0
                    for carte in liste_pioche:
                        if valeurCarte(carte) == i + score_croupier:
                            count += 1
                    pourcentage_mise_joueur = 0
                    for nom in scores:
                        if scores[nom]["score"] == score_croupier + i:
                            pourcentage_mise_joueur += scores[nom][
                                "mise_round"] / (mise_round_total + 1)
                    liste_pioche_pourcentage.append(
                        (count / (len(liste_pioche) + 1)) *
                        (1 + pourcentage_mise_joueur))
                success_rate_pioche = 0
                for liste_pioche_pourcentage_element in liste_pioche_pourcentage:
                    success_rate_pioche += liste_pioche_pourcentage_element
                if success_rate_pioche > 0.6:
                    score = croupier_prendre_carte(liste_pioche, 1)
                    print("Son score est maintenant de %s points." % score)
                    score_croupier += score
                valeur_croupier = score_croupier
                print("Le croupier a un score de %s points." % valeur_croupier)
                for nom in scores:
                    scores[nom]["croupier_value_final"] = valeur_croupier
                if score_croupier > 21:
                    for nom in scores:
                        if scores[nom]["out"] == False:
                            scores[nom]["success"] = True
                            mise_round = scores[nom]["mise_round"]
                            scores[nom]["mise"] += mise_round
                            scores[nom]["point"] += 1
                        scores[nom]["croupier_value_final"] = score_croupier
                    return
                else:
                    nom, score = gagnant(scores, valeur_croupier)
                    for nom_gagner_plus_point in nom:
                        for nom in scores:
                            if nom == nom_gagner_plus_point:
                                scores[nom_gagner_plus_point]["success"] = True
                                scores[nom_gagner_plus_point]["point"] += 1
                                mise_round = scores[nom_gagner_plus_point][
                                    "mise_round"]
                                scores[nom_gagner_plus_point][
                                    "mise"] += mise_round * 2
                                print("%s, vous avez gagné!" %
                                      nom_gagner_plus_point)
                    return
        elif count_out == len(scores):
            # Cest a dire que tous les personnes sont out
            print("Le croupier a gagné!")
            return
        else:
            for nom in scores:
                if not scores[nom]["give_up"] and not scores[nom][
                        "success"] and not scores[nom]["out"] and not scores[
                            nom]["draw"]:
                    tourJoueur(liste_pioche, nom, scores,
                               score_croupier_premier_round)


def croupier_prendre_carte(liste_pioche, nombre):
    """ Cette méthode permet au croupier de tirer une carte, d'imprimer le numéro de la carte et de renvoyer ce numéro.

    Args:
        liste_pioche (list): Liste de carte
        nombre (int): Nombre de cartes à tirer

    Returns:
        int: Valeur de la carte tirer
    """
    if liste_pioche == []:
        liste_pioche = initPioche(len(scores))
    liste_carte = piocheCarte(liste_pioche, nombre)
    score = 0
    for carte in liste_carte:
        print("Le croupier a pioché : %s" % carte)
        score += valeurCarte(carte)
    return score


def bot_decision_multitask(database, liste_pioche, scores, nom, i):
    """ Cette approche consiste à attribuer des tâches différentes à chaque cœur afin d'améliorer l'efficacité du calcul de l'IA.

    Args:
        database (dict): Résultats historiques des excursions précédentes
        liste_pioche (list): Liste de carte
        scores (dict): Dictionnaire des scores
        nom (str): Nom du joueur
        i (int): Numéro du tour

    Returns:
        int: Chances de gagner
        int: Chances de perdre
        int: Chances de gagner pour tirer une carte avec une valeur i
        int: Chances de perdre pour tirer une carte avec une valeur i
        float: Chances de tirer cette carte
    """
    # i 是下张什么牌
    score = scores[nom]["score"]
    length = 21 - score - 1

    success = 0
    defayant = 0
    success_prochain = 0
    defayant_prochain = 0

    carte = score + i

    # find carte in piochelist
    carte_total = len(liste_pioche)
    count = 0  # count combien de carte dans la pioche
    for carte_pioche in liste_pioche:
        if i == 1:
            i = 0  # Cas A
        if valeurCarte(carte_pioche) == i:
            count += 1
    if carte_total == 0:
        carte_total = 1
    probabilite = (count / carte_total)
    for item in database:
        list_temp_2 = []
        success_bool = database[item]["success"]
        for j in range(int(database[item]["round"]) - 1):
            list_temp_1 = []

            for key, item_score in database[item]["score"].items():
                list_temp_1.append(int(item_score))

            list_temp_2.append([list_temp_1[j], list_temp_1[j + 1]])
            if carte in list_temp_1:
                if success_bool:
                    success_prochain += 1
                else:
                    defayant_prochain += 1
        for k in range(len(list_temp_2)):
            if list_temp_2[k][0] == carte:
                if list_temp_2[k][1] > 21:
                    out = True
                else:
                    out = False

                feature_liste = [
                    int(list_temp_2[k][0]), out, database[item]["success"]
                ]
                if feature_liste[1]:
                    defayant += 1
                else:
                    success += 1
    return success, defayant, success_prochain, defayant_prochain, probabilite


def bot_decision(liste_pioche, scores, nom):
    """ Cette fonction est une fonction qui permet à l'ordinateur de déterminer si une carte a été tirée.

    Args:
        liste_pioche (list): liste de carte
        scores (dict): dictionnaire des scores
        nom (str): nom du joueur

    Returns:
        bool: prendre carte ou pas
    """
    database = read_history("INF101/TP/Projet Final/history.txt")
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
        # poursentage_de_mise = scores[nom]["mise_round"] / scores[nom]["mise"]

        length = 21 - score - 1
        win_rate = pg.plot()
        win_rate.setWindowTitle('Win Rate Bar Graph')
        x = np.arange(length)
        x = x + score + 1

        success_rate_list = []
        success_rate_list_prochaine = []
        success_list_out = []
        defayant_list_out = []
        success_list_prochain = []
        defayant_list_prochaine = []
        probabilite_list = []
        param_dict = {}

        num_cores = int(mp.cpu_count())
        pool = mp.Pool(processes=num_cores - 2)
        # pool = mp.Pool(4)
        for i in range(1, 21 - score):
            if i > 10:
                i = 1

            param_dict[i] = [scores, nom, i]
            # if feature_liste[1]:
            #     defayant_list[i - 1] += 1
            # else:
            #     success_list[i - 1] += 1
        results = [
            pool.apply_async(bot_decision_multitask,
                             args=(database, liste_pioche, scores, nom, i))
            for i in range(1, 21 - score)
        ]
        results = [p.get() for p in results]
        for result in results:
            success_list_out.append(result[0])
            defayant_list_out.append(result[1])
            success_list_prochain.append(result[2])
            defayant_list_prochaine.append(result[3])
            probabilite_list.append(result[4])

        for i in range(len(success_list_out)):
            success_rate_list.append(
                success_list_out[i] /
                (success_list_out[i] + defayant_list_out[i] + 1))

        for i in range(len(success_list_prochain)):
            success_rate_list_prochaine.append(
                success_list_prochain[i] /
                (success_list_prochain[i] + defayant_list_prochaine[i] + 1))

        win_rate.plot(x=x,
                      y=success_rate_list_prochaine,
                      symbolBrush=(255, 0, 0),
                      symbolPen='w')
        pg.exec()

    success_rate_final = 0
    for j in range(len(success_rate_list)):
        poid = 1 / (2 * (j + 1))
        success_rate_final += success_rate_list[j] * (probabilite_list[j] +
                                                      1) * poid
    print("Success rate: %s" % success_rate_final)
    # time.sleep(0.01)

    if success_rate_final >= 0.2:
        return True
    else:
        return False


def read_database(path):
    """ Cette méthode est utilisée pour lire la base de données locale

    Args:
        path (str): Le chemin correspondant au fichier

    Returns:
        dict: Retourner la base de données convertie
    """
    database = {}
    count = 0
    for line in open(path, "r"):
        line = line[:-1]  # delete \n
        # list_chaque_personne = f.split("\n")
        database[count] = {}
        item_list = line.split(",")
        database[count]["round"] = int(item_list[0])
        database[count]["score"] = {}
        for score in item_list[1:-3]:
            list_temp = score.split(":")
            database[count]["score"][list_temp[0]] = int(list_temp[1])
        database[count]["success"] = bool(
            distutils.util.strtobool(item_list[-3]))
        database[count]["out"] = bool(distutils.util.strtobool(item_list[-2]))
        database[count]["give_up"] = bool(
            distutils.util.strtobool(item_list[-1]))
        count += 1
    return database


def read_history(path):
    """ Cette méthode est utilisée pour lire la histoire locale

    Args:
        path (str): Le chemin correspondant au fichier

    Returns:
        dict: Retourner la histoire convertie
    """
    history = {}
    count = 0
    for line in open(path, "r"):
        line = line[:-1]  # delete \n
        # list_chaque_personne = f.split("\n")
        history[count] = {}
        item_list = line.split(",")
        history[count]["round"] = int(item_list[0])
        history[count]["croupier_premier_round"] = int(item_list[1])
        history[count]["croupier_value_final"] = int(item_list[2])
        history[count]["score"] = {}
        for score in item_list[3:-4]:
            list_temp = score.split(":")
            history[count]["score"][list_temp[0]] = int(list_temp[1])
        history[count]["success"] = bool(
            distutils.util.strtobool(item_list[-4]))
        history[count]["out"] = bool(distutils.util.strtobool(item_list[-3]))
        history[count]["give_up"] = bool(
            distutils.util.strtobool(item_list[-2]))
        history[count]["draw"] = bool(distutils.util.strtobool(item_list[-1]))
        count += 1
    return history


# def show_history():
#     global win_rate
#     win_rate.clear()
#     history = read_history("INF101/TP/Projet Final/history.txt")
#     x = np.arange(17)
#     x += 4
#     success_rate_list_point = []
#     for number in range(4, 21):
#         success = 0
#         defayant = 0
#         for item in history:
#             temp_list_1 = []
#             for key, item_score in history[item]["score"].items():
#                 temp_list_1.append(int(item_score))
#             if number in temp_list_1:
#                 if history[item]["success"]:
#                     success += 1
#                 else:
#                     defayant += 1
#         success_rate_list_point.append(success / (success + defayant + 1))
#     bargraph = pg.BarGraphItem(x=x,
#                                height=success_rate_list_point,
#                                width=1,
#                                brush='b')
#     win_rate.addItem(bargraph)

if __name__ == "__main__":
    history = read_history("INF101/TP/Projet Final/history.txt")
    # win_rate = pg.plot()
    # win_rate.setWindowTitle('Win Rate Bar Graph')
    # timer = pg.QtCore.QTimer()
    # timer.timeout.connect(show_history)
    # timer.start(1000)
    # pg.exec()

    # app = QApplication(sys.argv)
    # window = QWidget()
    # window.setWindowTitle('Application')
    # layout = QFormLayout()
    # layout.addRow("Nombre du joueurs", QLineEdit())
    # layout.addRow("Nombre de ordi", QLineEdit())
    # btns = QDialogButtonBox()
    # btns.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

    # window.setLayout(layout)
    # window.show()
    
    nombre_de_personne = int(input("Combien y-a-t il de joueurs?"))
    nombre_de_ordi = int(input("Combien y-a-t il d'ordi?"))


    liste_joueurs = initJoueurs(nombre_de_personne)
    liste_ordi = initOrdi(nombre_de_ordi)
    liste_pioche = initPioche(nombre_de_personne)
    scores = initScores(liste_joueurs, liste_ordi, 0)

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
        scores = initScores(liste_joueurs, liste_ordi, 0)
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
            if scores[nom]["ordi"] == False:
                print(
                    "%s: Vous avez actuellement %s $." % (nom, scores[nom]["mise"]))
                mise_round = int(input("%s, Combien voulez-vous miser?" % nom))
                while mise_round > scores[nom]["mise"]:
                    mise_round = int(
                        input(
                            "Vous n'avez pas cette somme.\n%s, Combien voulez-vous miser?"
                            % nom))
                scores[nom]["mise_round"] = mise_round
                scores[nom]["mise"] -= mise_round
            else:
                mise = scores[nom]["mise"]
                if mise > 10:
                    mise_round = random.randint(1, int(mise / 2))
                else:
                    mise_round = mise
                scores[nom]["mise_round"] = mise_round
                scores[nom]["mise"] -= mise_round
                print("%s mise %s" % (nom, mise_round))
        scores = premierTour(liste_pioche, scores)
        for nom in scores:
            if scores[nom]["score"] == 21:
                scores[nom]["success"] = True
                scores[nom]["blackjack"] = True
                scores[nom]["point"] += 1
                scores[nom]["mise"] += (scores[nom]["mise_round"]) * 2.5
        print(len(liste_pioche))
        tourComplet(liste_pioche, scores)
        path = os.path.join("INF101", "TP", "Projet Final", "history.txt")
        for nom in scores:
            if scores[nom]["history"] != []:
                history_save_to_txt(path, scores[nom])
        continuer = input("Voulez-vous rejouer? y ou n")
        if continuer == "n":
            dict_point = {}
            dict_mise = {}
            for nom in scores:
                dict_point[nom] = scores[nom]["point"]
                dict_mise[nom] = scores[nom]["mise"]
            print(dict_point)
            exit()
        # else:
        #     # scores = gestion_de_la_partie.rejouer(scores)
        #     dict_point = {}
        #     for nom in scores:
        #         dict_point[nom] = scores[nom]["point"]
        #     print(dict_point)
        #     scores = premierTour(liste_joueurs)
        #     for nom in scores:
        #         scores[nom]["point"] = dict_point[nom]

# gestion_de_la_partie.bot_decision("history.txt", scores, "a")
