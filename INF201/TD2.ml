(*2.6*)
(*let (bi, bs) = i in
  or let (precede (x:int) (bi, bs:intervelle))*)
type intervalle = int * int;;
let dans (x:int) (i:intervalle) :bool=
  let(bi, bs) = i in
  x >= bi && x <= bs;;

let precede (x:int) (i:intervalle):bool=
  let (bi, _) = i in
  x < bi;;

let suit (x:int) (bi, bs:intervalle):bool=
  not (precede x (bi, bs)) && not (dans x (bi, bs));;

let coteAcote (bi1, bs1:intervalle) (bi2, bs2:intervalle):bool =
  bi2 = bs1 + 1 || bi1 = bs2 + 1;;

let chvauche (bi1, bs1:intervalle) (bi2, bs2:intervalle):bool =
  bi1 < bi2 && bs1 < bs2 && bi2 < bs1 || bi2 < bi1 && bs2 < bs1 && bi1 < bs2;;


(*2.3*)
type heure = int (* 0, 11*);;
type minute = int;;
type seconde = int;;
type meridien = Am|Pm;;

type horaire = heure * minute * seconde * meridien;;

let inc_hor (h, m, s, mer:horaire):horaire =
  if s = 59 then
    if m = 5 then
      if h = 11 then
        if mer = Am then
          (0, 0, 0, Pm)
        else
          (0, 0, 0, Am)
      else
        (h+1, 0, 0, mer)
    else
      (h, m+1, 0, mer)
  else
    (h, m, s+1, mer);;


let ajout3sec (hor:horaire): horaire =
  inc_hor(inc_hor(inc_hor hor));;

ajout3sec 11 11 11 Am;;
