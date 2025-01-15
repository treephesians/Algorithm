import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# Step 1: A와 B의 모든 합을 계산하여 빈도 저장
sum_ab = defaultdict(int)
for a in A:
    for b in B:
        sum_ab[a + b] += 1

# Step 2: C와 D의 모든 합의 음수 값을 찾아 빈도 누적
answer = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in sum_ab:
            answer += sum_ab[target]

print(answer)