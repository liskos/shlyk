import sys
file = open("Задание 24/24.txt",mode="r",encoding = "utf8")

sys.stdin = file

k = 0
for s in file:
    k += s.count("X"*6)
    k += s.count("Y"*3)
    k += s.count("Z"*9)
print(k)
