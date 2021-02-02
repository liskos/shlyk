import sys
file = open("Задание 26/26.txt",mode="r",encoding="utf8")
sys.stdin = file
n,k = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
otl = a[:k]
hor = a[k:k*2]
print(sum(hor)//k)
print(sum(otl)//k)
