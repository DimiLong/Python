from sys import argv
script, hours, ratePerHour, prize = argv
def isFloat(value):
    ret = True
    for c in value:
        if not c.isdigit() and c != '.' and c != ',':
            ret = False
            break
    return ret
def calc(hours, ratePerHour, prize):
    return hours * ratePerHour + prize
print(ratePerHour.isnumeric())
if isFloat(hours) and isFloat(ratePerHour) and isFloat(prize):
    hours = hours.replace(',', '.')
    ratePerHour = ratePerHour.replace(',', '.')
    prize = prize.replace(',', '.')
    print(calc(float(hours), float(ratePerHour), float(prize)))
else:
    print('Аргументы должны быть числами')