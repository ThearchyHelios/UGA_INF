<!--
 * @Author: JIANG Yilun
 * @Date: 2021-12-17 21:40:39
 * @LastEditTime: 2021-12-17 21:46:16
 * @LastEditors: JIANG Yilun
 * @Description: 
 * @FilePath: /UGA_INF/INF101/TP/Projet Final/README.md
-->
[![BlackJack](https://img.shields.io/badge/BlackJack-black.svg)](https://github.com/Marshellson/Cinematheque)
[![Maintaner](https://img.shields.io/badge/Maintainer-JIANGYilun_AYIGAHSokem-blue)](https://github.com/Marshellson/UGA_INF/graphs/contributors)


# Projet final - Jeu du Blackjack

## Sommaire
[Introduction]
[Le jeu du Blackjack]
[Règles du jeu]
Objectifs du projet
Réalisation du Blackjack
Initialisations et gestion
Intelligences artificielles
Taux de réussite B – IA des joueurs C – IA du croupier
Conclusion
Améliorations envisageables B – Bilan


## Introduction

### Le jeu du Blackjack

Le Blackjack est un jeu d’argent qui vit le jour en France, entre le 17e et le 18e siècle. A l’origine, le valet noir octroyait aux joueurs un bonus, d’où le nom Blackjack qui a été maintenu, bien que le bonus ait été modifié. Rapidement, le jeu fut très apprécié des amateurs de casino, notamment grâce à ses règles, qui se trouvent être plutôt simples.

### Règles du jeu

Il existe de nombreuses variantes du jeu mais nous nous intéresserons ici à une version simplifiée des règles.
Chaque joueur joue individuellement contre la banque, qui est incarnée par le croupier. Le but est d’obtenir un score plus élevé que le croupier, sans jamais dépasser les 21 points. On joue avec des paquets de 52 cartes (autant de paquets que de joueurs) qui ont les valeurs suivantes :
- Les cartes numérotées de 2 à 10 valent autant de points que leur numéro; - Les têtes (valet, dame et roi) valent 10 points;
- L’as vaut 1 ou 11 points au choix;
Le score d’un joueur est égal à la somme de la valeur des cartes qu’il possède.

Au début du tour, chaque joueur mise la somme qu’il souhaite. Le croupier distribue ensuite deux cartes face visible à chacun d’entre eux, et une à lui-même. Si un joueur reçoit un as et une carte de valeur 10, il obtient alors un ‘‘blackjack’’, et remporte immédiatement son duel face au croupier, et remporte 2,5 fois sa mise de départ. Les joueurs choisissent un à un de s’arrêter ou de piocher une carte supplémentaire, action qui peut être répétée autant de fois que voulu, mais attention, si un joueur dépasse les 21 points, il est éliminé.
Une fois que tous les joueurs ont fini de piocher, c’est au tour du croupier de jouer. Il pioche une carte, puis joue avec les mêmes restrictions. Après cela, tous les joueurs ayant un score supérieur à celui du croupier récupèrent leurs mises respectives x2, et les autres la cèdent à la banque. En cas d’égalité, le joueur récupère sa mise une fois seulement.

### Objectifs

Ce projet consiste à développer en python une version fonctionnelle du Blackjack. Pour ce faire, nous suivrons l’énoncé en quatre parties qui nous a été proposé, tout en laissant libre cours à notre imagination, pour obtenir la version qui nous convient le mieux.
Les principaux objectifs du projet :
- Utiliser les différentes connaissances et notions acquises tout au long de l’UE
pour créer un jeu.
- Comprendre et traduire en algorithme les règles du black jack.
- Écrire un code efficace, lisible et compréhensible, grâce aux annotations.
- Apprendre et découvrir de nouvelles fonctions du langage Python, pour améliorer
notre code.

## Réalisation du Blackjack

### Initialisations et gestion

Comme indiqué dans le poly, nous avons commencé par créer toutes les fonctions nécessaires au bon fonctionnement du programme. Chacune d’entre elles sont commentées dans le programme, avec ses arguments, ses sorties et son rôle. On peut trier nos fonctions en différentes catégories que voici :

Les fonctions de bases (communes à toutes les version du jeux) :
- paquet
- valeurCarte - initPioche
- piocheCarte, - initJoueurs
- initOrdi
- initScors
- premierTour
- gagnant
- joueur_continuer - tourJoueur
- tourComplet

Toutes ces fonctions sont décrites dans le code. Avec elles, il est envisageable de coder une première version du jeu, ou les joueurs jouent les uns contre les autres, sans mises, ni croupier. Après cela, nous avons modifié le code pour permettre aux joueurs de miser.

Les fonctions d’historique (pour créer une base de données et l’exploiter) :
- history_save_to_txt
- read_database
- read_history

Ces fonctions nous permettent de créer un historique des parties, qui nous sera utile pour la réalisation de nos intelligences artificielles. Si l’historique n’est pas assez grand, les IA utiliseront la base de données, réalisée au préalable avec 250,000 essais.
Les fonctions d’IA (utilisées pour les différentes difficultés du croupier) :
- croupier_easy
- croupier_normal
- croupier_hard
- croupier_prendre_carte
- bot_decision_multitask
- bot_decision

Les fonctions d’IA seront décrites plus en détail dans la partie 3.

## Intelligences artificielles
Pour obtenir une version finale du jeu, on ajoute des IA (Intelligences artificielles). Pour les coder, nous avons fait des recherches et nous nous sommes appuyés sur différents ouvrages, dont une grande partie faisait référence à l'utilisation des méthodes de Monte Carlo, et de la formule de Kelly.

### Taux de réussite

Grâce à nos recherches et nos tests, nous avons pu identifier certains facteurs qui influent sur le pourcentage de taux de réussite (chances de gagner) du joueur.

Le joueur joue avant le croupier. Il peut donc être éliminé immédiatement en dépassant les 21 points, et céder sa mise à la banque, sans que le croupier n’ait eu besoin de jouer. Cette règle est particulièrement dangereuse pour le joueur, lorsque son score de départ est compris entre 12 et 17 points, car la prochaine carte déterminera alors s’il est éliminé ou non. Le graphique ci-dessous nous montre clairement que le joueur a un pourcentage de réussite bien plus faible dans ce cas précis.

