import sys
file = open("Задание 24/24.txt", mode="r", encoding="utf8")
sys.stdin = file

s = input()
mas = set(s)
for i in mas:
    k = i
    while k in s:
        k = k + i
    print(len(k)-1)