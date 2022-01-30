let abs = fun (a:int) -> if a < 0 then -a else a;;
Printf.printf"%i" (abs (-433));;
print_newline();;
let carre n = n * n ;;
let carre (n : int):int = n * n;;
Printf.printf"%i" (carre(-3));;
(fun (a : int) -> if a < 0 then -a else a) (-2);;
let aire (a:float) (b:float) = a *. b;;
let aire (a:float) (b:float):float = a *. b;;
(aire(2.3) (1.7));;

(* if conction then expr1 else expr2 *)


let maximeme (a:int) (b:int):int =
  if a>b then a else b;;

let maximeme_plus_1 (a:int) (b:int):int =
  (maximeme a b) + 1;;

maximeme_plus_1 2 3;;
let abs(e:int) : int =
  if e < 0 then -e else e;;
