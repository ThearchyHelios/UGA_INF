'''
Author: JIANG Yilun
Date: 2021-09-21 09:05:28
LastEditTime: 2021-10-06 10:04:00
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TD/1.3.7.py
'''
# temp = []
# sum = 0
# for a in range(5):
#     temp.append(int(input("Saissez un nombre")))
# for i in temp:
#     sum += i
# print(sum)

# for i in temp:
#     if (i % 2 != 0):
#         print("%s est impair" % i)

# print(temp)

from itertools import count

n = int(input("Saissez un nombre: "))
somme = 0
i = 1

while i <= n:
    somme += i
    i += 1

print("La somme des %i entiers est: %s" % (n, somme))

somme = 0
i = 1

while i <= n:
    if (i % 2 != 0):
        somme += i
    i += 1

print("La somme des %i entiers impaire est: %s" % (n, somme))

somme = 0
i = 1

while True:
    x = int(input("Entrer un entier: "))
    somme += x
    count += 1
    c = input("Une nouvelle valeur? y ou n")
    if c == 'n':
        break
print("La somme des %i entiers est: %s" % (n, somme))