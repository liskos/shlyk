def func(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 9)
        x = x // 9
    return a,b


k = 0
l = 0
p = 0
for i in range(1000000):
    l,p = func(i)
    if l == 3 and p == 24:
        k = i
print(k)

