import datetime

annee_naissance = int(input("Quelle est ton annee de naissance? "))
now = datetime.datetime.now()
annee_current = now.year

print("En %s tu a " % annee_current, str(annee_current - annee_naissance))
