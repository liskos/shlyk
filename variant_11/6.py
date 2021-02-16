def fun(d):
    n = 7
    s = 35
    while s <= 2570:
        s = s + d
        n = n + 9
    return n


k = 0
for i in range(1,100000):
    if fun(i) == 196:
        k += 1
print(k)
