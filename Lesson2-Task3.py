#Через list
zima_list = (12, 1, 2)
vesna_list = (3, 4, 5)
leto_list = (6, 7, 8)
osen_list = (9, 10, 11)
vvod = int(input("Введите номер месяца:  "))
if vvod in zima_list:
    print("Зима")
elif vvod in vesna_list:
    print("Весна")
elif vvod in leto_list:
    print("Лето")
elif vvod in osen_list:
    print("Осень")

#Через dict
year_dict = dict(mes_1='Зима', mes_2='Зима', mes_3='Весна', \
                 mes_4='Весна', mes_5='Весна', mes_6='Лето', \
                 mes_7='Лето', mes_8='Лето', mes_9='Осень', \
                 mes_10='Осень', mes_11='Осень', mes_12='Зима')
key = "mes_" + (input("Введите номер месяца:  "))
print(year_dict.get(key))
