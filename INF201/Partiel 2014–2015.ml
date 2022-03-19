type platPrincipal = P1 | P2 | P3;;
type tailleEntree = Petite | Moyenne | Grande;;
type formage = M of int | P;;
type dessert = D1 | D2 | D3;;

type cout = int;;

let coutEntree tailleEntree =
  match tailleEntree with
    | Petite -> 3
    | Moyenne -> 5
    | Grande -> 7;;

let cstPRIXPRINCIPAL:cout = 10;;
let cstSUPLP3: cout = 3;;

let coutPrincipal platPrincipal =
  match platPrincipal with
  | P1 -> cstPRIXPRINCIPAL
  | P2 -> cstPRIXPRINCIPAL
  | P3 -> cstPRIXPRINCIPAL + cstSUPLP3;;

let formageUnite:cout = 2;;
let formagePlateau:cout = 6;;

let coutFormage formage =
  match formage with
  | M(value) -> formageUnite * value
  | P -> formagePlateau;;

coutFormage(M(12));;

let coutDessert dessert =
  match dessert with
  | _ -> 5;;

coutDessert(D1);;

type fromOUdess = D of dessert | F of formage;;

let coutFormOuDess fromOUdess =
  match fromOUdess with
  | F(value) -> coutFormage(value)
  | D(value) -> coutDessert(value);;

coutFormOuDess(D(D1));;
coutFormOuDess(F(M(12)));;

type repa = | F1 of tailleEntree * platPrincipal | F2 of platPrincipal * fromOUdess;;

let formule1:repa = F1(Petite, P3);;
let formule2:repa = F2(P1, F(M(1)));;

let coutRepa repa =
  match repa with
  | F1(taille, plat) -> coutEntree(taille) + coutPrincipal(plat)
  | F2(plat, fromOUdess) -> coutPrincipal(plat) + coutFormOuDess(fromOUdess);;
let coutFormule1 = coutRepa(formule1);;
let coutFormule2 = coutRepa(formule2);;

