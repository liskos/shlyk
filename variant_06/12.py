x = "1"*84
while "11111" in x or "888" in x:
    if "11111" in x:
        x = x.replace("11111",'88',1)
    elif "888" in x:
        x = x.replace('888','88',1)
print(x)
