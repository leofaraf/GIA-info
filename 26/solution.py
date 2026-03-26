f = open("inf_22_10_20_26.txt")
n = int(f.readline())

sum = 0
maxdis = 0

first = True

for line in f.readlines():
    num = int(line)


    if num > 50:
        if not first:
            maxdis = max(maxdis, num)
            discounted = num * 0.75
            sum += discounted
    else:
        sum += num
    if first:
        first = False
    else:
        first = True

print(round(sum), maxdis)
f.close()