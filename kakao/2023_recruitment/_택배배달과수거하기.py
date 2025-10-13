def solution(cap, n, deliveries, pickups):
    answer = 0
    d_sum, p_sum = 0, 0
    
    # 뒤에서부터
    for i in range(n - 1, -1, -1):
        d_sum += deliveries[i]
        p_sum += pickups[i]
        
        # 이 위치까지 아직 처리할 게 있다면
        while d_sum > 0 or p_sum > 0:
            d_sum -= cap
            p_sum -= cap
            answer += (i + 1) * 2  # 왕복 거리
    return answer