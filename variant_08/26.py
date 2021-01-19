import sys
text = open("Задание 26/26.txt",mode="r",encoding="utf8")
sys.stdin = text


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(a)
a.sort()
print(a)
k = n // 20
b = a[k:-k]
print(b)
print(sum(b))
print(max(b))
