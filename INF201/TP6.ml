type flux = int;;
type releve = V | C of flux * releve;;

let nbj_sans_1 (releve) = 0;;

type resultat = R1 | R2 | R3;;

(* let rec nbj_sans_2 (releve:releve) : resultat =
  match releve with
   *)

let rec nbj_avec (x:flux) (r:releve) :int =
  match r with
  | C(y, z)-> if x = y then x else nbj_avec x r
  | V -> if x = 0 then x else nbj_avec x r;;

nbj_avec 3 (C(3, C(5, C(6, V))));;
