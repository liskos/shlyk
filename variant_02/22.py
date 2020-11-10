def func(x):
    a, b = 0, 0
    while x > 0:
        a = a + 1
        b = b +(x % 8)
        x = x // 8
    return a,b


j = []
for i in range(1,10000):
    a,b = func(i)
    if a == 3 and b == 12:
        j.append(i)
print(max(j))

