viruchka = int(input("Введите значение выручки: "))
izdergki = int(input("Введите значение издержки: "))
if viruchka > izdergki:
    print("Фирма работает с прибылью!")
    pribl = viruchka - izdergki
    print("Рентабельность составляет: ", "{:.3f}".format(pribl/viruchka))
    sotrudniki = int(input("Введите количество сотрудников: "))
    print("Прибыль на одного сотрудника сотавляет: ", "{:.2f}".format(pribl / sotrudniki))
else:
    print("Фирма работает с убытком!")

