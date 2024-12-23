import sys

input = sys.stdin.readline

N = int(input())

x_arr = []
y_arr = []

for _ in range(N):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_arr.append(x_arr[0])
y_arr.append(y_arr[0])

sum1 = 0
sum2 = 0
for i in range(N):
    sum1 += x_arr[i] * y_arr[i + 1]
    sum2 += y_arr[i] * x_arr[i + 1]

answer = round(abs(sum1 - sum2) / 2, 1)
print(answer)