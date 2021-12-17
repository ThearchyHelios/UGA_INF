import math

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))

delta = (b * b) - 4 * a * c
racineDeDelta = math.sqrt(delta)

if delta > 0:
    x1 = (-b + racineDeDelta) / (2 * a)
    x2 = (-b - racineDeDelta) / (2 * a)
    print("Two solutions %s %s" % (x1, x2))
elif delta == 0:
    x = (-b) / (2 * a)
    print("Une solution %s" % x)
elif delta < 0:
    print("No solution")
