def variant1(x, y):
    ret = x
    level = y
    if level < 0:
        level *= -1
    for i in range(1, level):
        ret *= x
    if y < 0:
        ret = 1 / ret
    return ret
def variant2(x, y):
    return x ** y
print(variant1(4, -2))
print(variant1(4, 3))
print(variant2(4, -2))
print(variant2(4, 3))