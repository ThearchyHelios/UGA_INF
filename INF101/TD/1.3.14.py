n = float(input("Saissez un nombre n"))

tmp = 0


def trouve_nombre_or(range):
    table = []
    count = 0
    table.append(1)
    table.append(1)
    while True:
        tmp = table[count + 1] + table[count]
        table.append(tmp)
        nombre_or = table[len(table) - 2] / table[len(table) - 1]
        print(nombre_or)
        if range > abs(nombre_or - 0.618033988749895):
            return table, nombre_or
        else:
            count += 1


table, nombre_or = trouve_nombre_or(n)

print("Derniere Nombre: %s" % table[len(table) - 1])
print(table)
print("Nombre d'Or: %s" % nombre_or)
