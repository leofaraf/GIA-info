def F(x, y, A):
    return ((x + y) < 54) or (x <= (y-3)) or (x > A)

for A in range(2000, 1, -1):
	OK = all(F(x, y, A) for x in range(1000) for y in range(1000))
	if OK:
		print(A)
		break