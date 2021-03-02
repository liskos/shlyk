import sys
file = open("Задание 27/27-B.txt",mode="r",encoding="utf8")
sys.stdin = file

n = int(input())
s = 0
razn = 99999
for i in range(n):
    a,b = map(int,input().split())
    s += min(a,b)
    if a != b:
        razn = min(razn, abs(a - b))
if s % 10 == 0:
    s += razn
print(s)




