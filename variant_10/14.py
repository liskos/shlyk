s = (4**14) + (64**16) - 81
b = ""
while s > 0:
    b = str(s % 4) + b
    s = s // 4
print(b.count("3"))
