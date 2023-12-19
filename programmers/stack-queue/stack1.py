def solution(arr):
    
    answer = []
    pre_num = -1

    for this_num in arr:
        if pre_num != this_num:
            answer.append(this_num)
            pre_num = this_num
        if pre_num == this_num:
            continue

    return answer


arr = [1,1,3,3,0,1,1,4,4]

print(solution(arr))