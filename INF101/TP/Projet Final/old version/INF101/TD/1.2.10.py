a = int(input("A: "))
b = int(input("B: "))
c = int(input("c: "))
max = int

if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c

print("Maximem number: %s" % max)

# Version 2

x = int(input("X: "))
max = x
y = int(input("Y: "))
if y > max:
    max = b
z = int(input("Z: "))
if z > max:
    max = z

print("Maximem number: %s" % max)