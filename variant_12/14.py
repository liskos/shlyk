s = 81**17 + 3**24 - 45
n = ""
while s > 0:
    n = str(s % 9) + n
    s = s // 9
print(n.count("8"))