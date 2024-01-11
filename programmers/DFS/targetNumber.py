def dfs(numbers, i, result, target):
    if i < len(numbers):
        number =  numbers[i]
        dfs(numbers, i + 1, result + number, target)
        dfs(numbers, i + 1, result - number, target)
    else:
        if result == target:
            global answer 
            answer += 1

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, 0, 0, target)
    return answer

#1
numbers = [1,1,1,1,1]
target = 3

#2
numbers = [4, 1, 2, 1]
target = 2

print(solution(numbers, target))