let estJDM(jour:int) (mois:int):bool = 
  if mois == 2 && jour < 28 || (mois == 4 || mois == 6 || mois == 9 || mois == 11) && jour <= 30 || (mois == 1 || mois == 3 || mois = 5 || mois == 7 || mois == 8 || mois == 10 || mois == 12) && jour <= 31 then true else false;;

let c = 2 and d = 4. in (c+2, d);;
