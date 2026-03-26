ct = 0

for i in range(10000, 100000):
    istr = oct(i)[2:]
    сtt = 0
    ycor = True

    for c in range(2,len(istr)):
        if istr[c] == '2':
            if c+1 != len(istr) and istr[c+1] == '3':
                ycor = False
            сtt += 1
    
    if сtt == 2 and ycor:
        print(istr)
        ct+=1

print("ct", ct)