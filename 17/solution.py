f = open("17.txt")

arr = []

for line in f.readlines():
    arr.append(int(line))

minpos = 10001
maxrt = 0
ct = 0

for n in arr:
    if (str(n)[-1] == '3'):
        minpos = min(minpos, n)

for i in range(0, len(arr)-1):
    a = arr[i]
    b = arr[i+1]
    if (str(a)[-1] == '3') + (str(b)[-1] == '3') == 1:
        if (a + b) ** 2 >= abs(minpos):
            ct += 1
            maxrt = max(maxrt, (a + b)**2)

print(ct, maxrt)
f.close()