def func(x):
    a = []
    for i in range(2,x):
        if x % i == 0:
            a.append(i)
    return a




for i in range(19960,20000+1):
    mass = func(i)
    if len(mass) == 2:
        print(mass,mass[0]*mass[1])