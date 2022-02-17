(*Exercice 2.11*)
type jour =  int;;
type heure = int;;
type minute = int;;
type seconde = int;;

type duree = jour * heure * minute * seconde;;

let div (n:int) (d:int): int*int =
  n / d, n mod d;;

