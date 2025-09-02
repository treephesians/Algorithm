def solution(diffs, times, limit):
    def can_clear(level):
        new_limit = limit
        num = len(diffs)
        for i in range(num):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1] if i != 0 else 0
            time = time_cur if level >= diff else time_cur + (time_cur + time_prev) * (diff - level)
            new_limit -= time
            if new_limit < 0:   # 중간에 이미 초과하면 바로 종료 → 더 최적화
                return False
        return True
    
    # level의 탐색 범위 설정 (최대 난이도 이상이면 항상 가능)
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_clear(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer