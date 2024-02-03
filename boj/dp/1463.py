import sys

n = int(sys.stdin.readline())

answer = 0

while True:
    if n == 1:
        print(answer)
        break
    answer += 1
    if n % 3 == 0:
        n /= 3
    elif n % 2 == 0:
        if (n / 2) % 2 == 0:
            n /= 2
        elif (n - 1) % 3 == 0:
            n -= 1
        else:
            n /= 2
    else:
        n -= 1
        