a = 4**14 + 64**16 - 81
s = ""
while a > 0:
    s = str(a % 4) + s
    a = a // 4
print(s.count("0"))
