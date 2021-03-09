def f(x):
    a = []
    b = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
            if x // i % 2 == 0:
                a.append(x//i)
            else:
                b.append(x//i)
    return a, b


for i in range(326496, 649632 + 1, 2):
    masschet, massnechet = f(i)
    if len(masschet) == len(massnechet) >= 70:
        b = masschet + massnechet
        b.sort()
        for j in b:
            if j > 1000:
                print(i, j)
                break
