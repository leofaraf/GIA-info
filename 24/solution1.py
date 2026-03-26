f = open("24.txt")

s = f.readline()

maxstreak = 0
streak = 0
couter = 0

def isG(char):
    return char == 'A' or char == 'E'

while (couter < len(s)):
    maxstreak = max(maxstreak, streak)
    if isG(s[couter]) and not isG(s[couter+1]):
        streak += 1
        couter += 2
    else:
        couter += 1
        streak = 0

print(max(maxstreak, streak))

f.close()