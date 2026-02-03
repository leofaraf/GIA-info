def F(x, y, z, w):
    return (x and not y) or (y == z) or w

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not F(x, y, z, w):
                    print(x, y, z, w, 0)