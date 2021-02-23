def func(n):
    if n == 1:
        return 1
    elif n > 1 and n % 2 != 0:
        return n + func(n-2)
    elif n % 2 == 0:
        return n * func(n-1)


print(func(60))