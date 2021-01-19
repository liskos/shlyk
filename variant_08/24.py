import sys
file = open("Задание 24/24.txt",mode="r",encoding="utf8")
sys.stdin = file

f = input()
boss = f.count("BOSS")
jboss = f.count("JBOSS")
bossj = f.count("BOSSJ")
jbossj = f.count("JBOSSJ")
print(boss - (bossj+jboss-jbossj))
