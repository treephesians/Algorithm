# https://www.acmicpc.net/problem/15654

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for n in map(int,input().split()):
    arr.append(n)
arr.sort()

result = []

def dfs(n):
    result.append(n)
    if len(result) == M:
        print(" ".join(map(str, result)))
        result.pop()
    else:
        for i in arr:
            if i not in result:
                dfs(i)
        result.pop()

for i in arr:
    dfs(i)

