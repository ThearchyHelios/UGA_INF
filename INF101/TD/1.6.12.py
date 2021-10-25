import random

def une_partie(n):
    list_de = []
    for i in range(n):
        list_de.append(random.randint(1,6))
    return list_de


def competeur_face(liste_n_tirage):
    liste_de_compteur = [0,0,0,0,0,0]
    for e in liste_n_tirage:
        if(e > 6 or e < 1):
            print("L'element n'est pas correct")
        liste_de_compteur[e - 1]+= 1
    return liste_de_compteur



entier = int(input("Saissez un nombre"))
list_gerer = une_partie(entier)
print(list_gerer)
liste_de_compteur = competeur_face(list_gerer)
print(liste_de_compteur)