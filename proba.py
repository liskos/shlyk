for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            f = not (x or y) or (y == z)
            print(int(x), int(y), int(z), "|", int(f))
print("-------------")
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            f = not (x or y) or (y == z)
            if not f and not (x and not y and z):
                print(int(z), int(x), int(y), "|", int(f))
