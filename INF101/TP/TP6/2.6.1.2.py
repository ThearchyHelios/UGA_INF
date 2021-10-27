def proche_zero(list):
    temp_temperature = list[0]
    for i in range(len(list)):
        if abs(list[i]) < abs(temp_temperature):
            temp_temperature = list[i]
        if abs(list[i]) == abs(temp_temperature):
            if list[i] > temp_temperature:
                temp_temperature = list[i]
    return temp_temperature


list = [7, -10, 13, 8, 4, -7, -12, -3, 3, -9, 6, -1, -6, 7]
print(proche_zero(list))

