def myInput(inputMessage):
    val = 0
    while True:
        try:
            val = int(input(inputMessage))
            break
        except:
            print('Введено некорректное значение. Повторите ввод.')
    return val
while True:
    print('Для выхода введите В', 'Для вычисления введите К', sep = '\n')
    action = input().lower()
    if action == 'в':
        break;
    elif action == 'к':
        value1 = myInput('Введите делимое: ')
        value2 = myInput('Введите делитель: ')
        if value2 == 0:
            print('Делитель не может быть равен 0')
        else:
            print(value1, '/', value2, ' = ', value1 / value2)