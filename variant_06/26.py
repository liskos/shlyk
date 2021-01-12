import sys
file = open("Задание 26/26.txt")
sys.stdin = file
n,k = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
print(sum(a[:k]))