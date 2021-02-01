vvod = input("Введите целое положительное число: ")
proverkavvoda = int(vvod)
if proverkavvoda <= 0:
    print("Ошибка! Введен 0 или отрицательное число!")
else:
    vvodlist = [int(i) for i in list(vvod)]
    maxnum = 9
    while maxnum > 0:
        if (maxnum in vvodlist):
            print("Самая большая цифра в числе:", maxnum)
            break
        else:
            maxnum = maxnum - 1
