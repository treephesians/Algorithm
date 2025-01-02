import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터 초기화
start = 0
end = 0
current_sum = 0
min_length = float('inf')  # 최소 길이를 무한대로 초기화

while end < N:
    # 현재 합이 S 이상이 될 때까지 end를 이동
    current_sum += arr[end]
    
    while current_sum >= S:
        # 조건을 만족하면 최소 길이를 갱신
        min_length = min(min_length, end - start + 1)
        # start를 이동하며 윈도우 크기를 줄임
        current_sum -= arr[start]
        start += 1
    
    end += 1

# 결과 출력
if min_length == float('inf'):
    print(0)
else:
    print(min_length)