f = open("inf_22_10_20_24.txt")
counter = 0

for line in f.readlines():
    ect = line.count('E')
    act = line.count('A')
    
    if ect > act:
        counter += 1

print(counter)
f.close()