A = int(input("Entrer"))

n = 1
Un = A
Un_max = A
count_descente = 1
count_descente_max = 2
Un_prev = Un

while Un != 1:
    if Un % 2 == 0:
        Un = Un / 2
    else:
        Un = 3 * Un + 1
    n += 1
print("Un = 1 lorsque n eset egale a %i et la plus grand valeur atteint par la suite %i" % (n, Un_max))
