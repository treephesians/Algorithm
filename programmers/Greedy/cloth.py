def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for l in _lost:
        if l - 1 in _reserve:
            _reserve.remove(l - 1)
        elif l + 1 in _reserve:
            _reserve.remove(l + 1)
        else:
            n -= 1
    return n

#print(solution(5, [2,4], [1,3,5])) # 5
#print(solution(5, [2,4], [3])) # 4
#print(solution(3, [3], [1])) # 2
print(solution(5, [2,3,4], [1,3,5])) # 3