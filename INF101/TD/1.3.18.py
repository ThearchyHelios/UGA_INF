entier = int(input("Saissez un nombre: "))

for i in range(1, entier + 1):
    val = ""
    for j in range(1, i + 1):
        val += str(j) + " "
    print(val)

count_b = 0
for i in range(entier):
    val = ""
    for j in range(i + 1):
        count_b += 1
        val += str(count_b) + " "
    print(val)

count_c = entier
for i in range(1, entier + 1):
    val = ""
    for j in range(1, count_c + 1):
        val += str(j) + " "
    count_c -= 1
    print(val)

count_d = 0
for i in range(entier):
    val = ""
    for j in range(entier - i):
        count_d += 1
        val += str(count_d) + " "
    print(val)
