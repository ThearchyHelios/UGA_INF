prenom = input("Votre prenom svp ")

langue = input("Votre langue: ")  # Langue devait etre "francais" ou "anglais"

if langue == "francais":
    print("Bonjour %s" % prenom)
elif langue == "anglais":
    print("Hello %s" % prenom)
else:
    print("ERREUR")
