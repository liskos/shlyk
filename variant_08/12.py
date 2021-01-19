x = "563" * 121
while "56" in x or "3333" in x:
    x = x.replace("56","3",1)
    x = x.replace("3333","3",1)
print(x)