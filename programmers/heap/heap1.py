import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        #print(scoville)
        best_min = heapq.heappop(scoville)
        next_min = heapq.heappop(scoville)
        heapq.heappush(scoville, best_min + next_min * 2)
    
    if scoville[0] < K:
        answer = -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))