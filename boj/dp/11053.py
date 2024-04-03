import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

arr = [1 for _ in range(N)]



# 6
# 10 20 10 30 20 50
# answer = 4

# 6
# 10 30 20 30 20 50
# answer = 4

# 30 10 40 50 60 20 70

for i in range(N):
    now = A[i]
    for j in range(i+1, N):
        if A[j] > now and arr[j] <= arr[i] + 1:
            arr[j] = arr[i] + 1
            
print(max(arr))