a = []
for i in range(2476,7857+1):
    if (i % 2 == 0 and i % 8 != 0) and i // 100 % 10 <= 7:
        a.append(i)
print(len(a))
print((max(a)+min(a))/2)
