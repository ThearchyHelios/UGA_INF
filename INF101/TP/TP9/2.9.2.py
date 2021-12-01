'''
Author: JIANG Yilun
Date: 2021-12-01 12:50:18
LastEditTime: 2021-12-01 12:59:31
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/TP9/2.9.2.py
'''
from operator import concat
import random


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


def jeuComplexe(dictio: dict) -> None:
    count_round = 0
    count_success = 0
    while True:
        count_round += 1
        if jouerUnMot(dictio):
            count_success += 1
        continuer = input("Voulez-vous continuer? (o/n) ")
        if continuer == 'n':
            break

    print("Vous avez joué {} fois et avez réussi {} fois.".format(
        count_round, count_success))


jeuComplexe({'pomme': 'apple', 'orange': 'orange', 'banane': 'banana'})