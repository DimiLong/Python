s = 0
isExitCmd = 0
while isExitCmd == 0:
    try:
        for n in list(input('Введите числа разделенные пробелом: ').split()):
            if n == '#':
                isExitCmd = 1
            s += int(n)
    except ValueError:
        print('Введено некорректное значение...')
    print(s)
print(s)