import sys

N = int(sys.stdin.readline())

time_arr = list(map(int, sys.stdin.readline().split()))

time_arr.sort()

result = 0
for i in range(N):
    result += time_arr[i] * (N - i)

print(result)