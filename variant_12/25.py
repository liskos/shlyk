for i in range(123456789,223456789+1):
    k = []
    b = []
    for j in range(2,i):
        if i % j == 0:
            k.append(i)
    if len(k) == 3:
        print(i,k)






