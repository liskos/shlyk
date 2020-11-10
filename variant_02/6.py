def func(s):
    n = 0
    while s - n > 0:
        s = s - 10
        n = n + 15
    return n


a = []
for i in range(1, 10000):
    if func(i) == 165:
        a.append(i)
print(max(a))
