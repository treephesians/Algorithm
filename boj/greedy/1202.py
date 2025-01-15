import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

arr_jewel = []
arr_bag = []

for _ in range(N):
    M, V = map(int, input().split())
    arr_jewel.append((M, V))  # (무게, 가치)

for _ in range(K):
    C = int(input())
    arr_bag.append(C)

# 정렬
arr_jewel.sort()  # 무게를 기준으로 오름차순 정렬
arr_bag.sort()  # 가방 용량 기준으로 오름차순 정렬

max_heap = []
answer = 0
j = 0

# 작은 가방부터 탐색
for capacity in arr_bag:
    # 현재 가방에 넣을 수 있는 모든 보석을 힙에 추가
    while j < N and arr_jewel[j][0] <= capacity:
        heapq.heappush(max_heap, -arr_jewel[j][1])  # 힙에 가치를 음수로 넣어 최대 힙처럼 사용
        j += 1
    
    # 가장 가치가 높은 보석을 선택
    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)