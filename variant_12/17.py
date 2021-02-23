a = []
for i in range(200000, 400000 + 1):
    if i % 7 == 0 and i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0:
        a.append(i*100000)
print(len(a))
print(min(a))