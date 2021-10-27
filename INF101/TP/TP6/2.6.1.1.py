def minimun(list):
    for i in range(len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    return list[0]

def contains(list, element):
    if element in list:
        return True
    else:
        return False

def minimun2(list):
    for i in range(len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j] = key
    return list[1]

list = [2, 3, 5, 1, 7, 8, -1]
print(minimun(list))
print(contains(list, 1))
print(minimun2(list))