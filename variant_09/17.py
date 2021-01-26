a = []
for i in range(1016,7938):
    if i % 3 == 0 and not (i % 7 == 0 or i % 17 == 0 or i % 19 == 0 or i % 27 == 0):
        a.append(i)
print(len(a))
print(max(a))
