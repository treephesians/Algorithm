import sys

input = sys.stdin.readline
INF = int(1e9)
N, S = map(int, input().split())

arr = list(map(int, input().split()))

sum = 0
for i in range(len(arr)):
    sum += arr[i]
    arr[i] = sum

arr.insert(0, 0)

start = 0
end = 1
result = INF
while start != len(arr) - 2 and end != len(arr) - 1:
    if arr[end] - arr[start] < S:
        end += 1
    else:
        result = min(result, end - start)
        start += 1
        
if result == INF:
    print(0)
else:
    print(result)