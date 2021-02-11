from itertools import count
from itertools import cycle
def var1():
    for el in count(int(input('Введите стартовое число '))):
        print(el)
def var2():
    source_list = ['el1', 666, 'duck', (17, { 'product': 'uh' })]
    for el in cycle(source_list):
        print(el)
print('Вариант А введите 1','Вариант Б введите - 2', sep='\n')
s = input()
if s == '1':
    var1()
elif s == '2':
    var2()