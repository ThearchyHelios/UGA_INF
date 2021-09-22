import random


def jeu(a):
    nombre_saisser = a
    nombre_correct = random.randint(0, 100)
    nombre_temp_gauche = 0
    nombre_temp_droite = 100
    chance_rest = 5
    chance_utilise = 0
    correct = False
    while not correct:
        if nombre_saisser > nombre_correct:
            chance_rest -= 1
            chance_utilise += 1
            if chance_rest == 0:
                print("Vous n'avez pas le chance!")
                continuer = input("Vous voulais continuer? (o ou n)")
                if continuer == "o":
                    return chance_rest, chance_utilise, False, True
                else:
                    return chance_rest, chance_utilise, False, False
            nombre_temp_droite = nombre_saisser
            print("Trop grand (Chance rest: %i)" % chance_rest)
            print("Devine mon nombre entre %i et %i" % (nombre_temp_gauche, nombre_temp_droite))
            nombre_saisser = int(input("Saissez un nombre SVP: "))

        elif nombre_saisser < nombre_correct:
            chance_utilise += 1
            chance_rest -= 1
            if chance_rest == 0:
                print("Vous n'avez pas le chance!")
                continuer = input("Vous voulais continuer? (o ou n)")
                if continuer == "o":
                    return chance_rest, chance_utilise, False, True
                else:
                    return chance_rest, chance_utilise, False, False
            nombre_temp_gauche = nombre_saisser
            print("Trop petit (Chance rest: %i)" % chance_rest)
            print("Devine mon nombre entre %i et %i" % (nombre_temp_gauche, nombre_temp_droite))
            nombre_saisser = int(input("Saissez un nombre SVP: "))
        elif nombre_saisser == nombre_correct:
            chance_utilise += 1
            print("Ouii, le nomre est correst, il est %i !" % nombre_correct)
            continuer = input("Vous voulais continuer? (o ou n)")
            if continuer == "o":
                return chance_rest, chance_utilise, True, True
            else:
                return chance_rest, chance_utilise, True, False


chance_total_utilise = 0
chance_total_rest = 0
fois = 0
vectoire_fois = 0
while True:
    fois += 1
    nombre_saisser = int(input("Saissez un nombre SVP: "))
    (chance_rest, chance_utilise, vectoire, continuer) = jeu(nombre_saisser)
    if vectoire:
        vectoire_fois += 1
    if not continuer:
        print("Tu as gagné %s parties sur %s jouées, tu as mis en moyenne %s essais pour deviner" % (vectoire, fois, chance_utilise/(chance_utilise+chance_rest)))
        break
    chance_total_rest += chance_rest
    chance_total_utilise += chance_utilise
    print(chance_total_rest, chance_total_utilise, fois)
