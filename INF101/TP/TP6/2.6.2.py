list = []
while True:
    a = int(input("Saissez un nombre positive, ou saisser 0 pour arreter"))
    if a > 0:
        list.append(a)
    elif a < 0:
        print("POSITIVE!!!")
    else:
        break

temp = 0
for i in list:
    temp += i
moyenne = temp / len(list)
print(moyenne)

list_invice = []
for i in range(len(list), 0, -1):
    list_invice.append(i)
print(list_invice)
