def add(array, value):
    index = 0
    for item in array:
        if item <= value:
            break
        else:
            index += 1
    array.insert(index, value)


my_list = [10, 7, 3, 1]
print(my_list)
try:
    val = int(input("value: "))
except:
    val = -1
while val > 0 or val == -1:
    if val != -1:
        add(my_list, val)
        print(my_list)
    try:
        val = int(input("value: "))
    except:
        val = -1