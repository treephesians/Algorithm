import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 배열 정렬

result = float('inf')  # 최소 값을 무한대로 초기화
answer = []

# 첫 번째 용액을 고정하고, 나머지 두 용액을 투 포인터로 탐색
for i in range(N - 2):
    fixed = arr[i]
    start, end = i + 1, N - 1
    
    while start < end:
        total = fixed + arr[start] + arr[end]
        
        # 0에 더 가까운 경우 갱신
        if abs(total) < abs(result):
            result = total
            answer = [fixed, arr[start], arr[end]]
        
        # 합이 0보다 작으면 start 증가
        if total < 0:
            start += 1
        # 합이 0보다 크면 end 감소
        elif total > 0:
            end -= 1
        else:
            # total이 정확히 0인 경우 최적이므로 종료
            print(*sorted([fixed, arr[start], arr[end]]))
            exit()

# 최적의 세 용액 출력 (오름차순)
print(*sorted(answer))