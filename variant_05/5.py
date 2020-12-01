def algor(n):
    a = list(map(int, str(n)))
    a.sort()
    big = a[2] * 10 + a[1]
    if a[0] != 0:
        little = a[0] * 10 + a[1]
        return big - little
    if a[1] != 0:
        little = a[1] * 10
        return big - little
    return 0

a = []
for i in range(800, 900+1):
    if algor(i) == 30:
        a.append(i)
print(a)
print(len(a))
