def f(n):
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    return a


x = 0
massivx = []
for i in range(541,1234+1):
    mas = f(i)
    if len(mas) > len(massivx):
        x = i
        massivx = mas
print(len(massivx),x)