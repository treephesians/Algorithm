'''
이것이 원래 기존 내 풀이
import sys

input = sys.stdin.readline

arr1 = list(input().strip())
arr2 = list(input().strip())

dp = [[{"length":0, "alphabets":""} for _ in range(len(arr1) + 1)] for _ in range(len(arr2) + 1)]


for i in range(1, len(arr2) + 1):
    for j in range(1, len(arr1) + 1):
        if arr1[j - 1] != arr2[i - 1]:
            if dp[i - 1][j]['length'] > dp[i][j - 1]['length']:
                dp[i][j]['length'] = dp[i - 1][j]['length']
                dp[i][j]['alphabets'] = dp[i - 1][j]['alphabets']
            else:
                dp[i][j]['length'] = dp[i][j - 1]['length']
                dp[i][j]['alphabets'] = dp[i][j - 1]['alphabets']
        else:
            dp[i][j]['length'] = dp[i - 1][j - 1]['length'] + 1
            dp[i][j]['alphabets'] = dp[i - 1][j - 1]['alphabets'] + arr1[j - 1]

print(dp[len(arr2)][len(arr1)]['length'])
print(dp[len(arr2)][len(arr1)]['alphabets'])
'''

import sys

input = sys.stdin.readline

arr1 = list(input().strip())
arr2 = list(input().strip())

# DP 테이블: LCS 길이만 저장
dp = [[0] * (len(arr1) + 1) for _ in range(len(arr2) + 1)]

# DP 배열 채우기
for i in range(1, len(arr2) + 1):
    for j in range(1, len(arr1) + 1):
        if arr1[j - 1] == arr2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 길이 출력
print(dp[len(arr2)][len(arr1)])

# LCS 문자열 복원 (Backtracking)
i, j = len(arr2), len(arr1)
lcs = []

while i > 0 and j > 0:
    if arr1[j - 1] == arr2[i - 1]:
        lcs.append(arr1[j - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

# 문자열 출력
print("".join(reversed(lcs)))