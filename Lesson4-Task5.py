from functools import reduce
def my_func(el_p, el):
    return el_p * el
source_list = [el for el in range(100, 1001) if el % 2 == 0]
mult = reduce(my_func, source_list)
print(f'Список четных значений', source_list)
print(f'Результат перемножения всех элементов списка', mult)