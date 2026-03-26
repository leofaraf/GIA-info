f = open("26.txt")

n = int(f.readline())

arr = []

for line in f.readlines():
    arr.append(int(line))

arr.sort()

isApl = False
lastNum = 0

print(arr)

dissum = 0
freect = 0

for n in arr:
    if lastNum == n:
        if isApl:
            dissum += n
            freect += 1
            isApl = False
        else:
            isApl = True
    else:
        isApl = True
        lastNum = n
print(dissum, freect)
f.close()