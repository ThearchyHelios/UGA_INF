'''
Author: JIANG Yilun
Date: 2021-10-05 09:11:58
LastEditTime: 2021-10-06 10:03:29
LastEditors: JIANG Yilun
Description: 
FilePath: /INF/INF101/TD/1.4.4.py
'''


def verication_mois(mois):
    mois_31 = [1, 3, 5, 7, 8, 10, 12]
    mois_30 = [4, 6, 9, 11]

    if(mois in mois_31):
        return "mois_31"
    elif(mois in mois_30):
        return "mois_30"
    else:
        return "Fevrier"


def verication_bord(jour, mois, annee):
    valide_date = True
