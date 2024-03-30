import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(1001)]

arr[1] = 1
arr[2] = 2
for i in range(3, n + 1):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 10007

print(arr[n] )