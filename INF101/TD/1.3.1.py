# Condition 1: Affiche 0 - 10
from time import process_time_ns

i = 0
while i <= 10:
    print(i)
    i += 1

# Condition 2: Affiche 10 - 0
i = 10
while i >= 0:
    print(i)
    i -= 1

# Condition 3: Affiche 3n (S < 30)
i = 0
while i < 30:
    print(i)
    i += 3

# Condition 4: Affiche 3 ^ n (S < 300)
i = 1
while i < 300:
    if (i == 1):
        print(i)
        i = 3
        continue
    print(i)
    i *= 3

# Condition 5: Affiche positive entier
i = int(input("Saissez un entier nombre: "))

while i > 0:
    print(i)
    break

# Condition 6: Affiche voyelle entier

i = input("Saissez un entier Character: ")

while i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    print(i)
    break

# Condition 7: Affiche voyelle entier
i = input("Saissez un entier Character(Condition7): ")
while True:
    if i in "aeiouy":
        print(i)
        break
    else:
        i = input("Saissez un entier Character(Condition7): ")
        continue
