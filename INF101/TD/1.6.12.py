from itertools import count
import random
from typing import Counter


def une_partie(n):
    list_de = []
    for i in range(n):
        list_de.append(random.randint(1, 6))
    return list_de


def competeur_face(liste_n_tirage):
    liste_de_compteur = [0, 0, 0, 0, 0, 0]
    for e in liste_n_tirage:
        if (e > 6 or e < 1):
            print("L'element n'est pas correct")
        liste_de_compteur[e - 1] += 1
    return liste_de_compteur


def etats_partie(liste):
    count = 0
    liste_etats = []
    for i in liste:
        count += i
    for i in liste:
        liste_etats.append(i / count * 100)

    return liste_etats


def face_gagnante(liste):
    # temp_key = 0
    # temp_value = 0
    # for i in range(len(liste)):
    #     if liste[i] > temp_value:
    #         temp_value = liste[i]
    #         temp_key += 1
    # return temp_key
    gagnante = 1
    liste_compteur_face = competeur_face(liste)
    nbr_apparu_max = liste_compteur_face[0]
    for i in range(1, len(liste_compteur_face)):
        if (nbr_apparu_max <= liste_compteur_face[i]):
            nbr_apparu_max = liste_compteur_face[i]
            gagnante = i + 1
    return gagnante


entier = int(input("Saissez un nombre"))
list_gerer = une_partie(entier)
print(list_gerer)
liste_de_compteur = competeur_face(list_gerer)
print(liste_de_compteur)
liste_etats = etats_partie(liste_de_compteur)

count = 1
for i in liste_etats:
    print(str(count), " - ", str(i) + "%")
    count += 1

le_plus_grand = face_gagnante(list_gerer)
print(le_plus_grand)
