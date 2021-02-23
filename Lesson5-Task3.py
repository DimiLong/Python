with open('employers.txt') as f:
    avg = 0
    count = 0
    for line in f:
        try:
            lastName, money = line.split()
            if int(money) < 20000:
                print(lastName)
            count += 1
            avg += int(money)
        except:
            print(f'Invalid line \'{line}\'.')
    print(f'average = {avg / count}')