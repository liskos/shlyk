def func(x):
    p = []
    for i in range(10,99+1):
        if x % i == 0:
            p.append(i)
    return p


for i in range(333555,777999+1):
    a = func(i)
    if len(a) == 35:
        print(i,min(a),max(a))