import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in map(int, input().split()):
    arr.append(i)

arr.sort()

result = []
answer = []

def sion(i):
    result.append(arr[i])
    if len(result) == M:
        answer.append("".join(map(str, result)))
        result.pop()
    else:
        for j in range(len(arr)):
            if i != j:
                sion(j)
                result.pop()
        result.pop()

beforeNum = 0
for i in range(len(arr)):
    if arr[i] != beforeNum:
        sion(i)
    beforeNum = i

answer = sorted(list(set(map(int, answer))))
for i in answer:
    print(" ".join(list(str(i))))

