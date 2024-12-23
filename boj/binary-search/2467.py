import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N - 1
sum = arr[start] + arr[end]
answer1 = arr[start]
answer2 = arr[end]
while start != end:
    result = arr[start] + arr[end]
    if abs(sum) >= abs(arr[start] + arr[end]):
        answer1 = arr[start]
        answer2 = arr[end] 
        sum = result
    if result < 0:
        start += 1
    elif result > 0:
        end -= 1
    elif result == 0:
        break

print(answer1, answer2)