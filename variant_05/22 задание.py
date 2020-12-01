def func(x):
    a = 0;
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += x % 8
        else:
            b *= x % 8
        x = x // 8
    return a,b


for i in range(1,5000):
    g,h = func(i)
    if g == 2 and h == 24:
        print(i)
        break