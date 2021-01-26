def func(a):
    for x in range(0,201):
        for y in range(0,201):
            f = (2*x + y != 100)or(x < y)or(a < x)
            if not f:
                return False
    return True


for a in range(0,1000000+1):
    if func(a):
        print(a)
