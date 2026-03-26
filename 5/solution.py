for i in range(0, 2000):
    dem = bin(i)[2:]
    sum = 0
    for n in range(2,len(dem)):
        sum += n

    if sum % 2 == 0:
        r = "10"+dem
        r = r[:-1] + '1'
    else:
        r = "1"+dem
        r = r[:-2] + '11'

    r10 = int(r, 2)

    print(i, dem, sum, r, r10)
    if r10 > 62:
        break