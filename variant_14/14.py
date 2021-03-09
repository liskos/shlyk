a = 3627 +618 - 19
b = ""
while a > 0:
    b = str(a % 6) + b
    a = a // 6
print(b)
print(b.count("0"))