def func(x):
    a = 0;
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    return a,b


l = ""
k = ""
for i in range(1000000):
    l,k = func(i)
    if l == 2 and k == 9:
        print(i)
        break
