def func(x):
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    return a,b
for i in range(9999):
    j,k = func(i)
    if j == 4 and k == 30:
        print(i)
        break
