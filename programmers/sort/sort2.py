def solution(numbers):
    answer = ''
    s = [str(i) for i in numbers]

    arr = []
    for i in range(len(s)):
        if len(s[i]) == 1:
            arr.append([s[i] * 4, 1])
        elif len(s[i]) == 2:
            arr.append([s[i] * 4, 2])
        elif len(s[i]) == 3:
            arr.append([s[i] * 4, 3])
        else:
            arr.append([s[i] , 4])
            
    arr.sort(key = lambda x:x[0], reverse=True)
    
    for i in range(len(arr)):
        if arr[i][1] == 1:
            answer += arr[i][0][0:1]
        elif arr[i][1] == 2:
            answer += arr[i][0][0:2]
        elif arr[i][1] == 3:
            answer += arr[i][0][0:3]
        else:
            answer += arr[i][0]
    
    return str(int(answer))
    
numbers = [6, 10, 2]
numbers = [0,1, 10,3, 3, 4, 30, 43, 432, 5, 890,881, 9, 999, 1000]
numbers = [1,1,1,1,32,321, 34, 4]
numbers = [1, 31, 311]
numbers = [31, 312]

print(solution(numbers))