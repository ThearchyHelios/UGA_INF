'''
Author: JIANG Yilun
Date: 2021-10-06 13:42:35
LastEditTime: 2021-10-06 16:30:40
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TP/TP1/2.3.2.py
'''

import turtle
import math
from rich.progress import track


def carre(x, y, longueur):
    turtle.goto(x, y)
    turtle.down()
    i = 1
    speed = 100
    while i <= 4:
        turtle.forward(longueur)
        turtle.right(90)
        i += 1
    turtle.up()


def circle(longueur):
    turtle.color('red', 'yellow')
    turtle.speed(-1)
    turtle.begin_fill()
    for i in track(range(200)):
        turtle.circle(longueur)
        longueur += 5
    turtle.end_fill()
    turtle.done()


# carre(0, 0, 50)
# carre(60, 0, 50)
# carre(120, 0, 50)
# carre(180, 0, 50)
# circle(10)

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# speed(-1)

# while track(True):
#     forward(200)
#     left(91)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


def circle_unfinie(x, y, distance, number):
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.color('red', 'yellow')
    turtle.speed(-1)
    for i in track(range(number)):
        turtle.circle(distance)
        turtle.right(360/number)
    turtle.up()
    turtle.end_fill()


x = 20

# turtle.setworldcoordinates(4 * x , 4 * x, 4 * x * (4 + 1), 4 * x * (3 + 1))
turtle.up()
for j in range(3):
    for i in range(4):
        circle_unfinie(4 * x * (i + 1), 4 * x * (j + 1), x, 1000)

# turtle.setworldcoordinates(3 * x  , 3 * x, 4 * x * (i), 4 * x * (j))


turtle.done()
