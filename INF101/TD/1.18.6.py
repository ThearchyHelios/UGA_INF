'''
Author: JIANG Yilun
Date: 2021-11-30 08:10:55
LastEditTime: 2021-11-30 09:15:12
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TD/1.18.6.py
'''


def changeUnChiffre(nombre: int) -> int:
    if nombre >= 5:
        nombre = nombre * 2 - 9
    else:
        nombre = nombre * 2
    return nombre


def changeChiffres(liste: list) -> list:
    for i in range(len(liste)):
        if i % 2 == 1:
            liste[-(i + 1)] = changeUnChiffre(liste[-(i + 1)])
    return liste


def resteDivSomme(liste: list) -> int:
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
    return somme / 10


def verifie_Luhn(numero) -> bool:
    verifie = (numero % 1 == 0)
    return verifie


def ajoute_chiffre_controle(list_numero: list) -> list:
    verifie = verifie_Luhn(resteDivSomme(changeChiffres(list_numero)))
    # if not verifie:
    #     verifie = False
    #     list_numero.append(0)
    #     while not verifie:
    #         list_numero[-1] += 1
    #         verifie = verifie_Luhn(resteDivSomme(list_numero))
    if not verifie:
        numero = int(resteDivSomme(list_numero) * 10)
        list_numero.append(10 - (numero % 10))
    return list_numero


if __name__ == "__main__":
    liste = [9, 7, 2, 4, 8, 7, 0, 8, 6]

    print(ajoute_chiffre_controle(liste))
