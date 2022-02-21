(*Exercice 2.11*)
type jour =  int;;
type heure = int;;
type minute = int;;
type seconde = int;;

type duree = jour * heure * minute * seconde;;

let div (n:int) (d:int): int*int =
  n / d, n mod d;;

let nb_total_sec jour heure minute seconde:int =
  seconde + minute * 60 + heure * 3600 + jour * 86400;;

nb_total_sec 1 0 0 0;;

(* let vec_en_duree  *)

let sec_en_duree seconde_total:duree =
  let jour, r_seconde = div seconde_total 86400 in
  let heure, r_seconde = div r_seconde 3600 in
  let minute, r_seconde = div r_seconde 60 in
  (jour, heure, minute, r_seconde);;

let duree_en_sec (d:duree):int =
  let jour, heure, minute, seconde = d in
  seconde + minute * 60 + heure * 3600 + jour * 86400;;
