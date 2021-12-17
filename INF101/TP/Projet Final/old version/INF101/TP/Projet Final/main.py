import initialisation
import gestion_de_la_partie


nombre_de_personne = int(input("Il y a combien de joueurs?"))

liste_pioche_chaque_personne = initialisation.initPioche(nombre_de_personne)

liste_joueurs = initialisation.initJoueurs(nombre_de_personne)
scores = initialisation.premierTour(liste_joueurs)

gestion_de_la_partie.tourComplet(scores, liste_pioche_chaque_personne)
