import sys
file = open("Задание 24/24.txt",mode = "r",encoding="utf8")

sys.stdin = file

s = input()
print(s)
x = "X" * 100000
while not x in s:
    x = x[1::]
print(x.count("X"))