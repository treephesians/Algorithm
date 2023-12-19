def solution(progresses, speeds):
    answer = []
    
    while(len(progresses) > 0):
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        done = 0
        while(progresses[0] >= 100):
            done += 1
            del progresses[0], speeds[0]
            if not progresses:
                break
        
        if done != 0:
            answer.append(done)

    return answer

progresses = [95, 90, 99, 99, 80, 99, 10]
speeds = [1, 1, 1, 1, 1, 1, 1]

progresses = [93, 30, 55, 10]
speeds = [1, 30, 5, 1]

print(solution(progresses, speeds))