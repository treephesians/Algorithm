def solution(clothes):
    answer = 1
    dic = {}
    for name, type in clothes:
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
    
    for num in dic.values():
        answer *= num + 1

    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))