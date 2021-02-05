keys = {'name': 'наименование', 'price': 'цена', 'qty': 'количесвто', 'unit': 'ед. из.'}


def inputNewGoods(id):
    dict_keys = {}
    for key, value in keys.items():
        while True:
            input_value = input('Введите ' + value + ' ')
            try:
                if key == 'price' or key == 'qty':
                    dict_keys[value] = int(input_value)
                else:
                    dict_keys[value] = input_value
                break
            except:
                print('Некорректное значение...')
    return (id, dict_keys)


def analysis(goods):
    ret_analysis = {}
    for value in keys.values():
        ret_analysis[value] = []

    for good in goods:
        for key, value in good[1].items():
            if not value in ret_analysis[key]:
                ret_analysis[key].append(value)

    print(ret_analysis)


def pringGoods(goods):
    for good in goods:
        print(good)


my_goods = []
last_index = 1
print('Для выхода введите В')
print('Для добавления товара введите Т')
print('Для аналитики введите А')
print('Для вывода товаров П')
action = input()
while action.lower() != 'в':
    if action.lower() == 'т':
        my_goods.append(inputNewGoods(last_index))
        last_index += 1
    elif action.lower() == 'п':
        pringGoods(my_goods)
    elif action.lower() == 'а':
        analysis(my_goods)
    print('----------')
    print('Для выхода введите В')
    print('Для добавления товара введите Т')
    print('Для аналитики введите А')
    print('Для вывода товаров П')
    action = input()
print('Пока')