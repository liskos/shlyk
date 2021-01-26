def func(a):
    h = []
    for i in range(2,a+1):
        if a % i == 0 and i % 2 == 1:
            h.append(i)
    return h



for i in range(123,1235):
    mass = func(i)
    if len(mass) == 4:
        print(i,mass)
