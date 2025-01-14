import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    start, end = map(int, input().split())
    arr.append((end, start))

arr.sort()
time = 0
answer = 0

while arr:
    end, start = arr.pop(0)
    if start >= time:
        answer += 1
        time = end

print(answer)