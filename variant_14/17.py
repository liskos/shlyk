count = 0
m = 0
for i in range(100001,900009+1):
    if i % 11 == 0 and i % 55 != 0:
        if (i % 7) + (i % 10) == 10:
            count += 1
            m = i
print(m,count)