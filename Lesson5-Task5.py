values = list(map(int, input('Введите список целых чисел разделенных пробелом: ').split()))
print('Запись в файл')
with open('integer_list.txt', 'w') as f:
    for value in values:
        f.write('%s ' % value)
print('Файл записан')
print('Чтение файла')
tempList = []
ret = 0
with open('integer_list.txt') as f:
    for line in f:
        tempList = list(map(int, line.split()))
        ret += sum(tempList)
print('Сумма чисел в файле:', ret)