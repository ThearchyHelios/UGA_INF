type nature123 = int;;
type sign = J | V | O | R of nature123;;

let sig_suivant sign :sign =
  match sign with
  | J -> V
  | V -> O
  | O -> R(3)
  | R(1) -> J
  | R(n) -> R(n-1);;


sig_suivant O;;
sig_suivant(R(3));;

(* let sig_compat (sign1:sign) (sign2:sign) :bool =
  match sign1 with
  | J -> match sign2 with
          | J -> false
          | V -> false
          | O -> false
          | R(n) -> true
          | _ -> false
  | V -> match sign2 with
          | J -> false
          | V -> false
          | O -> false
          | R(n) -> true
          | _ -> false
  | O -> match sign2 with
          | J -> false
          | V -> false
          | O -> false
          | R(n) -> false
          | _ -> false
  | R(n) -> match sign2 with
          | J -> false
          | V -> true
          | O -> false
          | R(n) -> false
          | _ -> false
  | _ -> false;; *)
  let sig_compat (sign1:sign) (sign2:sign) :bool =
    match sign1 with
    | J when sign2 = R(0) -> true
    | V when sign2 = R(0) -> true
    | O -> false
    | R(n) when sign2 = V -> true
    | _ -> false;;

sig_compat J (R(2));;
(* sig_compat (R(3)) V;; *)

type distance = Miles of float | Km of float;;
type unite_dict = Km | Miles;;
type distance2 = float * unite_dict;;

let a:distance = Km(1.0);;
let b:distance2 = (1.0, Km);;

let f x = 3 * x and g y = y + 4;;
(g 6) * (f 2);;

type etd = Age of int | Num_etd of int |Prenom of string | Nom of string;;

let edt1:etd = Age(18);;