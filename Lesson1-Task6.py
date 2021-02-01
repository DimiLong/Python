start = float(input("Сколько километров за первый день? "))
goal = float(input("Сколько километров в день планируется? "))
daykm = start
daynumber = 1
while goal > daykm:
    print(daynumber, "-й день:", "{:.2f}".format(daykm))
    daynumber = daynumber + 1
    daykm = daykm * 1.1
print(daynumber, "-й день:", "{:.2f}".format(daykm))
print("На", daynumber, "-й день будет достигнута цель")


