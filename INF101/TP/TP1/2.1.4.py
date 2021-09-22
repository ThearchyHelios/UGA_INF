# Programme valeur absolue
text = input("Donner un entier : ")
x = int(text)
text = input("Donner un entier : ")
y = int(text)
z = x - y

resultat = ""

if (z < 0):
    resultat = -z
else :
    z = resultat
    print("valeur absolue :", resultat)