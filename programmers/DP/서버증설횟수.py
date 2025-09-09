def solution(players, m, k):
    answer = 0
    server = [0 for _ in range(24)]
    
    for i in range(24):
        player = players[i]
        if player < m * (server[i] + 1):
            continue
        else:
            need_server = (player - m * server[i]) // m
            for j in range(k):
                if i + j >= 24: break
                server[i + j] += need_server
            answer += need_server
    
    return answer