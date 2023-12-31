def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0

    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            
        else:
            answer += 1
            if cur[0] == location:
                return answer


priorities = [1, 1, 9, 1, 1, 1]
queue =  [(i,p) for i,p in enumerate(priorities)]
print(queue)
location = 0
answer = 5

# solution(priorities, location)