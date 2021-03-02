import sys
file = open("Задание 24/24.txt")

for s in file:
    x = "X"
    while x in s:
        x += "X"
    y = "Y"
    while y in s:
        y += "Y"
    z = "Z"
    while z in s:
        z += "Z"
print(max(len(x), len(y), len(z))-1)