import sys
file = open("Задание 24/24.txt",mode="r",encoding = "utf8")

sys.stdin = file

k = 0
m = 0
for s in file:
    k += s.count("OCK")
    m += s.count("STOCK")
print(k - m)