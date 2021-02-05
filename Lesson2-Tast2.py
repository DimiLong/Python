vvod_spisok = input('Введите целые числа для списка через пробел: ').split()
chislo_par = len(vvod_spisok) // 2
a = 0
b = 1
num_par = 1
while chislo_par >= num_par:
    vvod_spisok[a], vvod_spisok[b] = vvod_spisok[b], vvod_spisok[a]
    a += 2
    b += 2
    num_par +=1
print(vvod_spisok)