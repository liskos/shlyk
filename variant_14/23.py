def f(a):
    if a == 2:
        return 1
    if a < 2:
        return 0
    else:
        return f(a-1) + f(a-3) + f(a//3)


print(f(22))