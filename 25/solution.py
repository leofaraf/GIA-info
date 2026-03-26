maxdiv = 0
num = 0

for i in range(568023, 569230+1):
    ict = 0

    for d in range(1, i+1):
        if i % d == 0:
            ict += 1


    print(i)
    if ict > maxdiv:
        maxdiv = ict
        num = i

print(maxdiv, num)