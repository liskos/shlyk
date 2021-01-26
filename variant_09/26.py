import sys
file = open("Задание 26/26.txt",mode = "r",encoding="utf8")


sys.stdin = file

n,k,m = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
print(a[k - 1])
print(a[k + m - 1])
