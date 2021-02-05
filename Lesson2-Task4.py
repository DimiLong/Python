vvod_spisok = input('Введите слова для списка через пробел: ').split()
num_stroki = 1
for i in vvod_spisok:
    print(num_stroki, i[:10])
    num_stroki += 1