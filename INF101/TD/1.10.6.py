'''
Author: JIANG Yilun
Date: 2021-12-01 13:35:28
LastEditTime: 2021-12-01 14:07:48
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TD/1.10.6.py
'''


def f(x:float)->float:
    y = 1.09 * x - 200
    return y

def nb_moustiques(nb_debut:float, annee_voulue:int)->float:
    nb_fin = nb_debut
    for i in range(annee_voulue - 2017):
        nb_fin = f(nb_fin)
    return nb_fin

def annee_atteindra(seuil:int, nb_debut:float)->int:
    annee = 2017
    while nb_debut < seuil:
        nb_debut = nb_debut * 1.09 - 200
        annee += 1
    return annee


nombre_actuel_marc = float(input("Entrez le nombre de moustiques actuel (Marc): "))
nombre_actuel_alice = float(input("Entrez le nombre de moustiques actuel (Alice): "))
annee_saissir = int(input("Entrez l'année voulue: "))

valeur_marc = nb_moustiques(nombre_actuel_marc, annee_saissir)
valeur_alice = nb_moustiques(nombre_actuel_alice, annee_saissir)
print(valeur_marc, valeur_alice)


seuil = float(input("Entrez le seuil: "))

annee_atteindra_marc = annee_atteindra(seuil, nombre_actuel_marc)
annee_atteindra_alice = annee_atteindra(seuil, nombre_actuel_alice)

print(annee_atteindra_marc, annee_atteindra_alice)