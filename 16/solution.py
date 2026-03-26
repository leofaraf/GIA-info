def F(n):
    r = 0
    while (n > 1):
        r += 3 * n
        n -= 1
    return r + 6
    
print(F(2023) - F(1984))