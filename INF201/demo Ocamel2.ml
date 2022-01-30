let racine (a:float) (b:float) (c:float): float*float=
  let delta = b *. b -. 4. *. a *. c in
  if delta >= 0. then
    ((-. b -. sqrt(delta)) /. (2. *. a), (-. b +. sqrt(delta)) /. (2. *. a))
  else
    failwith("Pas de racines");;

racine 1. 2. 1.;;
