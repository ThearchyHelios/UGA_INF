'''
Author: JIANG Yilun
Date: 2021-10-12 08:09:33
LastEditTime: 2021-10-12 09:07:46
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TD/1.4.12.py
'''

# a = int(input("Inserier A: "))
# b = int(input("Inserier B: "))


from pip import main


def soustraction(a, b):
    return a - b


def addition(a, b):
    return (soustraction(a, soustraction(0, b)))


def multiplication(a, b):
    somme = 0

    for i in range(b):
        somme = addition(somme, a)
    return somme


def division(a, b):
    q = 0
    while True:
        r = soustraction(a, b)
        q = addition(q, 1)
        if(r < b):
            break
    return q



print(division(6, 3))