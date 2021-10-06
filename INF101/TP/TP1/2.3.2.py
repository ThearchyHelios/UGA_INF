'''
Author: JIANG Yilun
Date: 2021-10-06 13:42:35
LastEditTime: 2021-10-06 14:39:57
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TP/TP1/2.3.2.py
'''

import turtle
import math
from rich.progress import track

def carre(x, y, longueur):
    i = 1
    speed = 100
    turtle.setx(x)
    turtle.sety(y)
    while i <= 4:
        turtle.forward(longueur)
        turtle.right(90)
        i += 1


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
circle(10)

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