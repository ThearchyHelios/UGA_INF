alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_alphabet = []
list_alphabet_cap = []
for i in alphabet:
    list_alphabet.append(i)
for i in alphabet_cap:
    list_alphabet_cap.append(i)

while True:
    a = input("saissez un mot: ")
    if a is not "":
        b = a.split(" ")
        print(b)
        for mot in b:
            list_nombre = []
            for i in mot:
                count = 0
                if i in alphabet:
                    for j in list_alphabet:
                        count += 1
                        if i == j:
                            list_nombre.append(count)
                            break
                else:
                    for j in list_alphabet_cap:
                        count += 1
                        if i == j:
                            list_nombre.append(count)
                            break
            for i in range(len(list_nombre) - 1):
                print(list_nombre[i], end="+")
            if mot == b[-1]:
                print(list_nombre[len(list_nombre) - 1], end="!\n")
            else:
                print(list_nombre[len(list_nombre) - 1], end=" ")

    else:
        break
