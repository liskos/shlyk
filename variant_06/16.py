def f(n):
    if n <= 2:
        return 3 * n - 3
    else:
        return f(n - 2) + 2 *f(n - 1) + 7


print(f(20))
