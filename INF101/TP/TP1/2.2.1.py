import math
from math import *
import random

x = log(2) + sqrt(exp(1)) * tan(pi / 8)
print(x)

longueur_hypothenuse = float(input("Entrez la longueur de l’hypothénuse:"))
valeur_angle = float(input("Entrez la valeur d’un angle:"))

print("Les deux côtés sont: %s , %s " % (
    longueur_hypothenuse * cos(valeur_angle), longueur_hypothenuse * sin(valeur_angle)))

x = random.randint(1, 4)
print("Random number: %i" % x)
