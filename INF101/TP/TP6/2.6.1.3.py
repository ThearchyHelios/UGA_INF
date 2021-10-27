def plus_proche_method_2(list, force):
    for i in range(len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    for i in range(len(list)):
        if list[i] == force:
            if i == 0:
                return list[i], list[i + 1]
            elif i == len(list) - 1:
                return list[i - 1], list[i]
            else:
                if list[i] - list[i - 1] < list[i + 1] - list[i]:
                    return list[i - 1], list[i]
                else:
                    return list[i], list[i + 1]

# def plus_proche_method_1(list):
#     for i in range(1, len(list)-1):
    


list = [2, 3, 5, 1, 7, 8, 12, 14]
list_temp = [9,2,6,8]

print(plus_proche_method_2(list_temp, ))