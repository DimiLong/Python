try:
    s = input('Введите список чисел разделеных пробелом ')
    source_list = list(map(int, s.split()))
    result_list = [el for el in source_list if source_list.count(el) == 1]
    print(result_list)
except Exception as e:
    print(e)