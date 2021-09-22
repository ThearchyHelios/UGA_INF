import random

fois_jouer = int(input("Combien de fois tu vous jouer?"))
nombre_fois_utilise = 0
nombre_maximeme = 100

for i in range(0, fois_jouer):
    nombre_random = random.randint(0, nombre_maximeme)
    print("Le nombre correst est %s" % nombre_random)
    nombre_temp_gauche = 0
    nombre_temp_droite = nombre_maximeme
    while True:
        nombre_temp_random = random.randint(nombre_temp_gauche, nombre_temp_droite)
        print("Je choisi %s" % nombre_temp_random)
        if nombre_temp_random < nombre_random:
            print("Cest trop petit")
            nombre_fois_utilise += 1
            nombre_temp_gauche = nombre_temp_random + 1
            print("Je vais essayer %s a %s\n" % (nombre_temp_gauche, nombre_temp_droite))
        elif nombre_temp_random > nombre_random:
            print("Cest trop grand")
            nombre_fois_utilise += 1
            nombre_temp_droite = nombre_temp_random - 1
            print("Je vais essayer %s a %s\n" % (nombre_temp_gauche, nombre_temp_droite))
        else:
            print("Yea, le bon reponse est: %s" % nombre_temp_random)
            nombre_fois_utilise += 1
            print("---------------------------------")
            break

print("En moyenne il utilise %s fois chaque question" % (nombre_fois_utilise/fois_jouer))