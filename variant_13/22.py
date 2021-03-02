def func(x):
    a = 0
    b = 0
    while x > 0:
        a += 1
        b += x % 8
        x = x // 8
    return a,b



for i in range(1,100000):
    a,b = func(i)
    if a == 3 and b == 21:
        print(i)


