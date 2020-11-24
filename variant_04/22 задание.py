def alg(x):
    Q = 7
    L = 0
    while L < x:
        L = L + Q
    L = Q - L + x
    if L == Q:
        L = 0
    M = (x - L) // Q
    if M < L:
        M, L = L, M
    return L,M


j = 0
for i in range(1,10000):
    a,b = alg(i)
    if a == 4 and b == 8:
        c = i
print(c)
