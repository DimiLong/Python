def getNewList(source_list):
    ret = []
    for idx in range(1, len(source_list)):
        if source_list[idx] > source_list[idx - 1]:
            ret.append(source_list[idx])
    return ret
try:
    s = input('Введите список чисел разделеных пробелом ')
    source_array = list(map(int, s.split()))
    print('Результат', getNewList(source_array))
except Exception as e:
    print(e)