import heapq

def solution(jobs):
    time = 0
    
    waiting_heap = []
    
    running = False
    n_process = len(jobs)
    turnaround_time = 0
    arrival_time = 0
    
    
    while True:
        # 시간이 됐는지 확인하고 waiting heap에 넣는 과정
        if jobs:
            while True:
                job = jobs.pop(0)
                if time == job[0]:
                    heapq.heappush(waiting_heap, [job[1], job[0]])
                else:
                    jobs.insert(0, job)
                    break
        
        # 한 process의 time이 끝날 때,
        # turnaround time 을 계산하고, waiting heap에 있는 process를 실행시킴
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

jobs = [[0, 3], [4, 9], [10, 6]]
print(solution(jobs))