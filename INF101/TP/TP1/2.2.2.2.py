import random

fois_jouer = int(input("Combien de fois tu vous jouer?"))

for i in range(0, fois_jouer):
    nombre_random = random.randint(0, 100)
    nombre_temp_gauche = 0
    nombre_temp_droite = 100
    while True:
        nombre_temp_random = random.randint(nombre_temp_gauche, nombre_temp_droite)
        if nombre_temp_random < nombre_random:
            nombre_temp_gauche = nombre_temp_random + 1
            print("Je vais essayer %s a %s" % (nombre_temp_gauche, nombre_temp_droite))
        elif nombre_temp_random > nombre_random:
            nombre_temp_droite = nombre_temp_random - 1
            print("Je vais essayer %s a %s" % (nombre_temp_gauche, nombre_temp_droite))
        else:
            print("Yea, le bon reponse est: %s" % nombre_temp_random)
            print("---------------------------------")
            break
