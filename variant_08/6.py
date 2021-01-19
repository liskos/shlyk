def fu(d):
    s, n = 0, 0
    while s < 111:
        s = s + 8
        n = n + d
    return n


l = ""
for i in range(100000):
    if fu(i) == 28:
        l = i
print(l)
