s = "1" + "0"*55
while "10" in s or '1' in s:
    if "10" in s:
        s = s.replace("10","001",1)
    elif "1" in s:
        s = s.replace("1","0",1)
print(s.count("0"))