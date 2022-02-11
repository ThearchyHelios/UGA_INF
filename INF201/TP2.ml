(*Question 2.4*)
(*Question 1*)

let a:int = 10;;
let b:int = 0;;

(b <> 0) && (a mod b == 0);;
(a mod b == 0) && (b <> 0);;
(*b <> 0  en premier, il est false donc a mod b == 0 ne fonction pas.*)

(*Question 2*)
let monExpression (a:int) (b:int) : bool =
  (b <> 0) && (a mod b = 0) ;;
monExpression 10 0;;

(*Question 3*)
let monEt(x:bool) (y:bool):bool =
  x && y;;

monEt true false;;
monEt false true;;
monEt (b <> 0) (a mod b = 0);;

(*Quand \(a mod b == 0\) comme un entier, il va toujour fonctionner.*)

(*Question 2.5*)
(*Question 1*)
3.5;; (*float*)
3,5;; (*int * int*)

(*Question 2*)
(4 + 3) / 2;; (*int = 3*)
(4 + 3) /. 2 ;; (*ERROR car le int ne peut utiliser le /.*)
(4.0 + 3.0) /. 2 ;; (*Error car le int ne peut utiliser le /.*)
(4.0 +. 3.0) /. 2 ;; (*ERROR parallels*)
(4.0 +. 3.0) /. 2.0 ;; (*float = 3.5*)

(*Conclusion: +. , /. peut utiliser juste pour les float, pas fonctionner pour int * float ou int * int*)

(*Question 3, 4*)
float_of_int 3;; (*float = 3*)
float_of_int 3.2;; (*ERROR le fonction float_of_int ne fonction pas pour les float*)

let moyenne (a:int) (b:int) : float =
  let a = float_of_int a in
  let b = float_of_int b in
  (a +. b) /. 2.0;;

(*Question 5*)
int_of_float (-1.9);; (*Il va prendre e valeur plus proche que 0*)

(*Question 2.6*)
(*Question 1*)
let min4 (a:int) (b:int) (c:int) (d:int) :int =
  if a < b && a < c && a < d then a
  else if b < a && b < c && b < d then b
  else if c < a && c < b && c < d then c
  else d;;

let max4 (a:int) (b:int) (c:int) (d:int) :int =
  if a > b && a > c && a > d then a
  else if b > a && b > c && b > d then b
  else if c > a && c > b && c > d then c
  else d;;

let max2 (a:int) (b:int):int =
  if a > b then a else b;;

let min2 (a:int) (b:int):int =
  if a < b then a else b;;

let moyol (a:int) (b:int) (c:int) (d:int) :int =
(*  let Min4 = min4 a b c d in
    let Max4 = max4 a b c d in*)
  (a + b + c + d - min4 a b c d - max4 a b c d) / 2;;

moyol 10 8 12 24;;

#trace min4;;
#trace max4;;
#trace moyol;;



(*Tracer est un dir pour debug*)
