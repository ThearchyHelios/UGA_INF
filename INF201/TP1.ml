"c" < "d";;
10 mod 5;;
10 mod 3;;
10 / 3;;
"D" < "c";;
false = (2 = 3);;
false = 2 = 3;;
2 = 3 = false;;
2 = 3 - 1 = 4 - 2;;

assert((5 = 3) = false);;
assert((5 = 5) = true);;
assert((5 = 4) = true);;

let a:int = 8;;
a;;
a = 5;;
a +. 9.1;;
float_of_int(a) +. 9.1;;

(*Q14*)

if a < 10 then true else a;;

if a < 10 then a else false;;

if a < 10 then a;;

if a < 10 then true else false;;

(*2.2.1*)

let max2(a:int) (b:int):int =
  ((a+b) + abs(a-b)) / 2;;

max2 3 4;;
max2 4 3;;

abs;;


(*Q5*)

let max3 (a:int) (b:int) (c:int):int =
  if a >= b && a >= c then a
  else if b >= a && b >= c then b
  else c;;

let max3_2 (a:int) (b:int) (c:int):int =
  if a > b
  then
  if a > c then a else c
  else
  if b > c then b else c;;

max3 5 6 7;;
max3_2 6 7 8;;

let max2 (a:int) (b:int):int =
  if a > b then a else b;;

let max3_3 (a:int) (b:int) (c:int):int =
  max2 a (max2 b c);;

let max3_4 (a:int) (b:int) (c:int):int =
  let m = max2 b c in
  if m > a then m else a;;
max3_4 6 7 8;;

let max3_4_prime (a:int) (b:int) (c:int):int =
  let m = if c > b then c else b in
  if a > m then a else m;;

max3_4_prime 1 2 3;;


let x=3 and y=4 in x+y;;
let x=3 and y=x+4 in x+y;;

let x=10 in
let x=3 and y=x+4 in
x + y;;

let x=10 in
(let x=3 and y=x+4 in x+y) + x;;
