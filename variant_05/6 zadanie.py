def func(d):
    s, k = 5, 0
    while s < d:
        k += 2
        s += k
    return s


for i in range(1,10000):
    if func(i) == 161:
        print(i)
        break