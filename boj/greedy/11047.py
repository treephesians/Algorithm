import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort(reverse=True)  # 큰 동전부터 사용

result = 0

for coin in arr:
    if coin <= K:
        result += K // coin
        K %= coin

print(result)