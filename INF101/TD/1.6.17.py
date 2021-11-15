def taille(a):
    liste_taille = []
    for i in a:
        count = 0
        for j in i:
            count += 1
        liste_taille.append(count)
    return liste_taille


def lire(a):
    liste = []
    for i in range(a):
        mot = input("Tapez un mot : ")
        liste.append(mot)
    return liste


def affiche(a):
    liste_taille = taille(a)
    count_taille = 0
    for i in liste_taille:
        count_taille += i

    for j in range(len(a)):
        print("Taille du mot %s : %s" % (a[j], liste_taille[j]))

    taille_moyenne = count_taille / len(a)
    print("Taille moyenne: ", taille_moyenne)
    print("Mots plus longs que la moyenne: ", end="")
    count_liste = 0
    for k in liste_taille:
        if k > taille_moyenne:
            print(a[count_liste], end="; ")
        count_liste += 1


def nbocc(a, b):
    count = 0
    for i in a :
        if i == b:
            count += 1
    return count


liste = ["adgwg", "wgwrgwgwrgw", "wgwr", "wyebfliwblwbflwb", "anloanfanofne"]
affiche(liste)
