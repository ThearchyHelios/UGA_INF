# import turtle
import math
import matplotlib.pyplot as plt


def capital(nb_years, start_capital):
    end_capital = 0
    for i in range(nb_years):
        if i == 0:
            end_capital = start_capital * 1.05 - 11
        else:
            end_capital = end_capital * 1.05 -11
    return end_capital


def money_earning(yr_year, start_capital):
    end_capital = 0
    for i in range(yr_year):
        if i == 0:
            end_capital = start_capital * 1.05 - 11
        else:
            end_capital = end_capital * 1.05 -11
    if end_capital < start_capital:
        return False
    else:
        return True


def investment_min(nb_years, goal):
    start_capital = 0
    point = []
    while True:
        start_capital += 1
        point.append(capital(nb_years, start_capital))
        if(capital(nb_years, start_capital))> goal:
            # plt.plot(point, "ro")
            # plt.plot(point)
            # plt.show()
            return start_capital


print(investment_min(1000, 100000))
print(capital(5, 832))