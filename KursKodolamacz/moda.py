def moda(lista: list) -> int:
    dict_1 = {}
    for i in lista:
        if i in dict_1.keys():
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    max_index = -1
    max_value = -1

    for k, v in dict_1.items():
        if v > max_value:
            max_value = v
            max_index = k

    return max_index


print(moda([4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 2, 1, 9, 8]))
