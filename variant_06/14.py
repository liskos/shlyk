x = (49**8)+(7**24)-749
s = ""
while x > 0:
    s = str(x % 7) + s
    x = x // 7
print(s)
print(s.count("6"))