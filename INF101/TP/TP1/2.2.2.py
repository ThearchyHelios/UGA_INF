import random

nombre_saisser = int(input("Saissez un nombre SVP: "))
nombre_correct = random.randint(0, 100)
nombre_temp_gauche = 0
nombre_temp_droite = 100

chance_rest = 5
chance_utilise = 0

corrrect = False


while not corrrect:
    if nombre_saisser > nombre_correct:
        chance_rest -= 1
        chance_utilise += 1
        if chance_rest == 0:
            print("Vous n'avez pas le chance!")
            break
        nombre_temp_droite = nombre_saisser
        print("Trop grand (Chance rest: %i)" % chance_rest)
        print("Devine mon nombre entre %i et %i" % (nombre_temp_gauche, nombre_temp_droite))
        nombre_saisser = int(input("Saissez un nombre SVP: "))

    elif nombre_saisser < nombre_correct:
        chance_utilise += 1
        chance_rest -= 1
        if chance_rest == 0:
            print("Vous n'avez pas le chance!")
            break
        nombre_temp_gauche = nombre_saisser
        print("Trop petit (Chance rest: %i)" % chance_rest)
        print("Devine mon nombre entre %i et %i" % (nombre_temp_gauche, nombre_temp_droite))
        nombre_saisser = int(input("Saissez un nombre SVP: "))
    elif nombre_saisser == nombre_correct:
        print("Ouii, le nomre est correst, il est %i !" % nombre_correct)
        corrrect = True
