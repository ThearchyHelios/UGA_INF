import random

x = random.randint(1, 6)

while True:
    print("x, ", x)
    if(x%2 != 0):
        x = random.randint(1, 6)
    else:
        break