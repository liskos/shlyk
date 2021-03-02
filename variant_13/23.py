def func(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return func(a+1,b)+func(a*2,b)


print(func(1,10)*func(10,21))
