def alg(s):
    n = 34
    while n <= 170:
        s = s + 120
        n = n + 23
    return(s)
for i in range(1,10000):
    if alg(i) >= 1000 and alg(i) <= 9999:
        print(i)
        break
