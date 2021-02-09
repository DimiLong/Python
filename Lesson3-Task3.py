def my_func(arg1, arg2, arg3):
    ret = 0
    if arg1 > arg3 and arg2 > arg3:
        ret = arg1 + arg2
    elif arg1 > arg2 and arg3 > arg2:
        ret = arg1 + arg3
    else:
        ret = arg2 + arg3
    return ret
print(my_func(9, 4, 2))
print(my_func(6, 2, 4))
print(my_func(5, 6, 14))
print(my_func(2, 3, 2))