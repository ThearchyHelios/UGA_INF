type jour = int;;
type mois = int;;

let estJourDansMois_2 jour mois:bool =
  if mois = 2 && (jour > 28 || jour <= 0) then false
  else if (mois = 1 || mois = 3 || mois = 5 || mois = 7 || mois = 8 || mois = 10 || mois = 12) && (jour > 31 || jour <= 0) then false
  else if (mois = 4 || mois = 6 || mois = 9 || mois = 11) && (jour <= 0 || jour > 30) then false
  else if mois <= 0 || mois > 12 then false
  else true;;

assert ((estJourDansMois_2 28 1) = true);;
assert ((estJourDansMois_2 29 2) = true);;
assert ((estJourDansMois_2 32 1) = true);;
assert ((estJourDansMois_2 31 9) = true);;
assert ((estJourDansMois_2 (-28) 11) = true);;
assert ((estJourDansMois_2 28 1) = true);;
estJourDansMois_2 29 2;;
estJourDansMois_2 0 4;;(*false, car j'ai defini le jour il faut >= 0*)

let  estJourDansMois_3 jour mois:bool =
  match mois with
  |1 | 3 | 5 | 7 | 8 | 10 | 12 when jour < 32 && jour > 0 -> true
  |4 | 6 | 9 | 11 when jour < 31 && jour > 0 -> true
  |2 when jour < 29 && jour > 0 -> true
  | _ -> false
;;
estJourDansMois_3 32 9;;
estJourDansMois_3 28 2;;
assert ((estJourDansMois_3 18 13) = true);;
assert ((estJourDansMois_3 0 4) = true);;

type mois = Janvier | Fevrier | Mars | Avril | Mai | Juin | Juillet | Aout | Septembre | Octobre | Novembre | Decembre ;;

let estJourDansMois_4 jours mois =
  match mois with
  |Janvier | Mars | Mai | Juillet | Aout | Octobre | Decembre when jours < 32 && jours > 0 -> true
  | Avril | Juin | Septembre | Novembre when jours < 31 && jours > 0 -> true
  | Fevrier when jours < 29 && jours > 0 -> true
;;
estJourDansMois_4 29 Fevrier;;
assert((estJourDansMois_4 0 Avril) = true);;
assert((estJourDansMois_4 29 Fevrier) = true);;

let div (n:int) (d:int): int*int =
  n / d, n mod d;;

for i = 1 to 9999 do
  if i = (sc i i) then Printf.printf "%i\n" i;
done
;;
div 9639;;
4 / 3;;


let sc(a:int) (b:int):int =
  let c, d = (div a b)in
  c + d;;
sc 4 5;;
div 4 5;;
sc 2345 5;;
