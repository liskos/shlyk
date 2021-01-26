a = 9**8 + 3**5 - 2
b = ""
while a > 0:
    b = str(a % 3) + b
    a = a // 3
print(b)
print(b.count("2"))