import heapq

def solution(jobs):
    time = 0
    
    waiting_heap = []
    
    running = False
    n_process = len(jobs)
    turnaround_time = 0
    arrival_time = 0
    
    while True:
        if jobs:
            while True:
                job = jobs.pop(0)
                if time == job[0]:
                    heapq.heappush(waiting_heap, [job[1], job[0]])
                else:
                    jobs.insert(0, job)
                    break
                if not jobs:
                    break
                
        if not running:
            if waiting_heap:
                waiting_job = heapq.heappop(waiting_heap)
                arrival_time = waiting_job[1]
                end_time = time + waiting_job[0]
                running = True
                
        if time == end_time:
            turnaround_time += end_time - arrival_time
            running = False
            if waiting_heap:
                waiting_job = heapq.heappop(waiting_heap)
                arrival_time = waiting_job[1]
                end_time = time + waiting_job[0]
                running = True
        
        if not running and waiting_heap:
            waiting_job = heapq.heappop(waiting_heap)
            arrival_time = waiting_job[1]
            end_time = time + waiting_job[0]
            running = True
        
        if not jobs and not waiting_heap and not running:
            break
        time += 1
            
    return turnaround_time // n_process

def other_solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))

jobs = [[0, 3], [1, 9], [2, 6]]
print(other_solution(jobs))