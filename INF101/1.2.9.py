import random

val_mes = float(input("Entrer une valeur"))
val_incertitude = float(input("Ebtrer l'incertitude associce"))
val_model = random.randint(1, 100)

# Version1

if val_model - val_mes < 2 * val_incertitude:
    print("Compatible")
else:
    print("Imcompatible")

# Version 2
if abs(val_model - val_mes) < val_incertitude:
    print("Compatible")
elif abs(val_model - val_mes) < 3 * val_incertitude:
    print("Incertain")
else:
    print("Imcompatible")
