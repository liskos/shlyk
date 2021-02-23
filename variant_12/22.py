def func(x):
    a = 1
    while x > 0:
        a *= x % 7
        x = x // 7
    return a


for i in range(1,10000):
    if func(i) == 48:
        print(i)
        break