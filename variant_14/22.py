def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 14 != 0:
            b = b * (x % 14)
        x = x // 14
    return a,b


k = 0
for i in range(1,99999):
    a,b = f(i)
    if a == 2 and b == 12:
        k += 1
print(k)
