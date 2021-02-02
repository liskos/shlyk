def func(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 9)
        x = x // 9
    return a,b


for i in range(1,100000):
    a,b = func(i)
    if a == 3 and b == 18:
        print(i)
        break