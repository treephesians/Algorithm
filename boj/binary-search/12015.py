import sys

input = sys.stdin.readline

# 이진 탐색 함수
def binary_search(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

# 입력
n = int(input())
a = list(map(int, input().split()))

# LIS 배열 유지
sub = []

for num in a:
    pos = binary_search(sub, num)  # 직접 구현한 이진 탐색 함수 사용
    if pos == len(sub):
        sub.append(num)  # 증가 수열 확장
    else:
        sub[pos] = num  # 수열 교체로 유지

# 결과 출력
print(len(sub))