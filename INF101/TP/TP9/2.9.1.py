'''
Author: JIANG Yilun
Date: 2021-12-01 12:26:56
LastEditTime: 2021-12-01 12:49:52
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/TP9/2.9.1.py
'''


def ajouteMot(dfren: dict, mfr: str, wen: str):
    dfren[mfr] = wen


def supprimeMot(dictionnaire: dict, mot: str):
    del dictionnaire[mot]


def afficheDico(dictionnaire: dict):
    for k, v in dictionnaire.items():
        print(k, " = ", v)


def afficheDicoLettre(dictio: dict, lettre: str):
    for k, v in dictio.items():
        if lettre in k:
            print(k, " = ", v)


def afficheDicoLongueur(dictionnaire: dict, longueur: int):
    for k, v in dictionnaire.items():
        if len(k) == longueur:
            print(k, " = ", v)


fr = {"livre":"book", "chien":"dog", "chat":"cat", "oiseau":"bird"}

ajouteMot(fr, "pomme", "apple")

afficheDico(fr)

print("\n")

supprimeMot(fr, "livre")

afficheDico(fr)