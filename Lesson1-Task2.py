vvod = int(input("Введите время в секундах: "))
if vvod >= 360000:
    print("Введите число поменьше!")
else:
    kolvochas = vvod // 3600
    if kolvochas < 1:
        kolvochas = 0
    ostatoksec = vvod - (kolvochas*3600)
    kolvomin = ostatoksec // 60
    if kolvomin < 1:
        kolvomin = 0
    kolvosec = ostatoksec - (kolvomin * 60)
    print("%02d" % kolvochas, ":", "%02d" % kolvomin, ":", "%02d" % kolvosec,)





