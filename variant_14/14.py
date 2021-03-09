a = 36**27 +6**18 - 19
b = ""
while a > 0:
    b = str(a % 6) + b
    a = a // 6
print(b)
print(b.count("0"))