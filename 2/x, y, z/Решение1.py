def F(x, y, z):
    return (x == z) or (x <= (y and z))

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not F(x, y, z):
                print(x, y, z, 0)