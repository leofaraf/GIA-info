counter = 0
i = 1987

while counter < 2 and i < 10**10:
    if i % 1987 == 0:
        s = str(i)
        if s[0] == '1' and s[2] == '6' and \
            s[3] == '1' and s[4] == '5' and \
            s[5] == '4' and s[-1] == '1':
            print(i, i//1987)
            counter += 1
    
    i += 1987