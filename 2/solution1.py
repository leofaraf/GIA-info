def f(x, y, z, w):
    return ((not w) or (not z)) and y and ((not x) or w)
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if f(x,y,z,w):
                    print(y,w,x,z,1)