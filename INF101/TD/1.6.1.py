
Multiple3 = [3, 6, 9, 15, 21]
print(Multiple3[2])
print(Multiple3)
Multiple3.append(12)
Multiple3.append(18)
print(Multiple3)

for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(i)
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(i, end=",")
print("\n")
list_alphabet = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    list_alphabet.append(i)

count = 0
while count < 26:
    print(list_alphabet[count], end=" ")
    count += 1
    if count % 10 == 0:
        print("")

print("")

list_nombre = [3, 3, 6, 9, 9]
list_nombre.pop(0)
print(list_nombre)

