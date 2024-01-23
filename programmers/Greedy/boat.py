from collections import deque

def solution(people, limit):
    
    answer = 0
    people.sort()
    q = deque(people)
    while q:
        first = q.pop()
        if q:
            second = q.popleft()
            if first + second > limit:
                q.appendleft(second)
        
        answer += 1
        
    return answer

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3
print(solution([20, 20, 20, 30, 40, 60, 70, 80], 100)) # 4