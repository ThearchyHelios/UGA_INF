'''
Author: JIANG Yilun
Date: 2021-12-01 13:01:29
LastEditTime: 2021-12-01 13:30:06
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/TP9/2.9.3.py
'''

import random


def initiale()->dict:
    nombre_de_personnes = int(input("Entrez le nombre de personnes: "))
    dict_personnes = {}
    for i in range(nombre_de_personnes):
        nom = input("Entrez le nom de la personne: ")
        dict_personnes[nom] = 0
    return dict_personnes



def traduire(dictio: dict, mot: str) -> str:
    for k, v in dictio.items():
        if mot == k:
            return v


def jouerUnMot(dictio: dict) -> bool:
    list_mot_francais = []
    for k, v in dictio.items():
        list_mot_francais.append(k)
    hasard_choisir = random.choice(list_mot_francais)
    mot_anglais_saissir = input("Entrez un mot anglais: ")
    if dictio[hasard_choisir] == mot_anglais_saissir:
        print("Bravo!")
        return True
    else:
        print("Dommage!")
        return False


dictionnaire = {'pomme': 'apple', 'orange': 'orange', 'banane': 'banana'}
nombre_round = int(input("Entrez le nombre de round: "))
dict_personnes = initiale()

for i in range(nombre_round):
    for nom in dict_personnes:
        print("cest le %s round du %s" % (i+1, nom))
        if jouerUnMot(dictionnaire):
            dict_personnes[nom] += 1

dict_pourcentage = {}
list_nom_ranking = []
list_score_ranking = []
for nom, score in dict_personnes.items():
    dict_pourcentage[nom] = (score / nombre_round) * 100
    list_nom_ranking.append(nom)
    list_score_ranking.append(score)


for i in range(len(list_nom_ranking)):
    for j in range(i+1, len(list_nom_ranking)):
        if list_score_ranking[i] < list_score_ranking[j]:
            list_score_ranking[i], list_score_ranking[j] = list_score_ranking[j], list_score_ranking[i]
            list_nom_ranking[i], list_nom_ranking[j] = list_nom_ranking[j], list_nom_ranking[i]

for i in range(len(list_nom_ranking)):
    print("{}: {}" % (list_nom_ranking[i], dict_pourcentage[list_nom_ranking[i]]), "%")