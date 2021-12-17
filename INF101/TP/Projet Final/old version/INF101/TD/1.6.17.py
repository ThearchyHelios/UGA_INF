def taille(a):
    liste_taille = []
    for i in a:
        count = 0
        for j in i:
            count += 1
        liste_taille.append(count)
    return liste_taille


def lire(n):
    liste = []
    for i in range(n):
        mot = input("Tapez un mot : ")
        liste.append(mot)
    return liste


def affiche(liste):
    liste_taille = taille(liste)
    count_taille = 0
    for i in liste_taille:
        count_taille += i

    for j in range(len(liste)):
        print("Taille du mot %s : %s" % (liste[j], liste_taille[j]))

    taille_moyenne = count_taille / len(liste)
    print("Taille moyenne: ", taille_moyenne)
    print("Mots plus longs que la moyenne: ", end="")
    count_liste = 0
    for k in liste_taille:
        if k > taille_moyenne:
            print(liste[count_liste] + ";", end="")
        count_liste += 1
    print("")

def nbocc(mot, car):
    count = 0
    for i in mot:
        if i == car:
            count += 1
    return count


def compteCarac(liste, car):
    count_total = 0
    liste_contient_car = []
    for mot in liste:
        temp = nbocc(mot, car)
        count_total += temp
        if temp != 0:
            print(mot)
            liste_contient_car.append(mot)

    if count_total != 0:
        print("Le caractère %s apparaît %s fois." % (car, count_total))
        return liste_contient_car
    else:
        print("Erreur la lettre %s n’est présente dans aucun des mots" % car)
        return False


def plusLongCarac(liste, car):
    liste_contient_car = compteCarac(liste, car)
    if not liste_contient_car:
        return
    nombre_carac_plus_grand = 0
    liste_mot_carac_plus_grand = []
    for mot in liste_contient_car:
        count = nbocc(mot, car)
        if count > nombre_carac_plus_grand:
            nombre_carac_plus_grand = count
    for mot in liste_contient_car:
        count = nbocc(mot, car)
        if count == nombre_carac_plus_grand:
            liste_mot_carac_plus_grand.append(mot)
    count_lettre_minimum = len(liste_mot_carac_plus_grand[0])
    for mot in liste_mot_carac_plus_grand:
        count_lettre = 0
        for lettre in mot:
            count_lettre += 1
        if count_lettre < count_lettre_minimum:
            count_lettre_minimum = count_lettre
    for mot in liste_mot_carac_plus_grand:
        count_lettre = 0
        for lettre in mot:
            count_lettre += 1
        if count_lettre == count_lettre_minimum:
            print("Le mot avec le plus caractere \"%s\" le plus court est : %s" % (car, mot))
            break


# liste = ["adgwg", "wgwrgwgwrgw", "wgwr", "wyebfliwblwbflwb", "anloanfanofne", "wwwww"]
# plusLongCarac(liste, "w")

if __name__ == '__main__':
    n = int(input("Saissez un nombre de fois"))
    liste = lire(n)
    while True:
        car = input("Saissez un caractere")
        affiche(liste)
        plusLongCarac(liste, car)
        print("--------------------")
