# +1
# *2
# +3


def solve(command, num):
    if command == 1:
        num = num - 4
    elif command == 2:
        num = num // 2

    if num == 10 or num < 2:
        return 0
    elif num == 2:
        return 1
    else:
        return solve(1, num) + solve(2, num)

print(solve(0, 74))