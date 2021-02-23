def f(s):
    n = 4
    while s < 37:
        s = s + 3
        n = n *2
    return n


for i in range(100000):
    if f(i) == 128:
        print(i)
        break