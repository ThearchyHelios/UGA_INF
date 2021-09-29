entier_L = int(input("Donner un entier L SVP"))

for i in range(entier_L):
    print("****")

for i in range(entier_L + 1):
    print("*" * i)

count_c = entier_L
for i in range(entier_L):
    count_c -= 1
    print(" " * count_c + "*" * (i + 1))

for i in range(entier_L):
    print("*" * (entier_L - i))

count_e = entier_L
for i in range(entier_L):
    print(" " * i + "*" * count_e)
    count_e -= 1

count_f = entier_L - 1
for i in range(entier_L):
    if i == entier_L - 1:
        print(" " * (count_f - i) + "*" * i + "o" + "*" * i + " " * (count_f - i))
        break
    print(" " * (count_f - i) + "*" * i + "*" + "*" * i + " " * (count_f - i))
