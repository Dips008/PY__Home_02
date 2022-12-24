# Реализуйте алгоритм перемешивания списка.

import random
lst = list(range(1, 10))
print(lst)


def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list


print(mix_list(lst))

random.shuffle(lst)
print(lst)
