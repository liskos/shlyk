c = []
for i in range(100000,1000000):
    a = i % 1000
    b = i // 1000
    if (a % 10) + (a % 100 // 10) + (a // 100) == (b % 10) + (b % 100 // 10) + (b // 100):
        c.append(i)
print(sum(c))