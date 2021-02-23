import sys
file = open("24/24.txt",mode="r",encoding="utf8")
sys.stdin = file

k = 0
for s in file:
    if s.count("E") > s.count("A"):
        k += 1
print(k)