def func(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return func(x + 1, y) + func(x * 3, y)
print(func(1,22)*func(22,70))