s = []
for i in range(1024,2048 + 1):
    if i % 7 == 0 and (i % 11 != 0 and i % 19 != 0):
        s.append(i)
print(len(s))
print(min(s))