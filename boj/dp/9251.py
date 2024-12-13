# https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline

arr1 = list(input())
arr2 = list(input())
arr1.pop()
arr2.pop()

index = 0
answer1 = 0
for i in range(len(arr1)):
    for j in range(index, len(arr2)):
        if arr1[i] == arr2[j]:
            answer1 += 1
            index = j + 1
            break

index = 0
answer2 = 0
for i in range(len(arr2)):
    for j in range(index, len(arr1)):
        if arr2[i] == arr1[j]:
            answer2 += 1
            index = j + 1
            break

print(max(answer1, answer2))