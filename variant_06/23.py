def func(a,b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif b % 2 == 0:
        return func(a,b - 1) + func(a,b - 2) + func(a,b//2)
    else:
        return func(a,b - 1) + func(a,b - 2)


print(func(3,9)*func(9,11)*func(11,12))