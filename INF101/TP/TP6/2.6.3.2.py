from collections import Counter

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_alphabet = []
list_alphabet_cap = []


while True:
    a = input("saissez un text svp: ")
    b = a.split(" ")
    if a == "":
        break
    list_count = []
    for mot in b:
        count = 0
        for i in mot:
            count += 1
        list_count.append(count)

    # print(list_count)
    count_maximem = list_count[0]
    temp_counter = 0
    for count in list_count:
        if count > count_maximem:
            count_maximem = count

    for i in list_count:
        if i == count_maximem:
            break
        temp_counter += 1

    mot_plus_long = b[temp_counter]
    print("the %s word is longest, it has %s numbers" %
          (mot_plus_long, count_maximem))

    sum_count = 0
    for count in list_count:
        sum_count += count
    count_moyenne = sum_count / count

    print("sum_count: ", sum_count)
    print("Count_moyenne: ", count_moyenne)
    print("Le(s) mots plus longs que la moyenne sont: ", end=" ")
    temp_counter = 0
    for i in list_count:
        if i >= count_moyenne:
            print(b[temp_counter], end=" ")
        temp_counter += 1
    print()

    mot_voyelle = "aeiouy"
    list_mot_voyelle = []
    for i in mot_voyelle:
        list_mot_voyelle.append(i)
    list_count_voyelle = []

    for i in range(len(b)):
        count_voyelle = 0
        for lettre in b[i]:
            if lettre in mot_voyelle:
                count_voyelle += 1
        list_count_voyelle.append(count_voyelle)

    mot_voyelle_maximeme = list_count_voyelle[0]
    for i in list_count_voyelle:
        if i > mot_voyelle_maximeme:
            mot_voyelle_maximeme = i

    temp_counter = 0
    for i in list_count_voyelle:
        if i == mot_voyelle_maximeme:
            break
        temp_counter += 1
    print("le mot qui contient le plus voyelle: ", b[temp_counter])
    print(list_count_voyelle)

    list = []
    for mot in b:
        for i in mot:
            list.append(i)
    print(Counter(list))