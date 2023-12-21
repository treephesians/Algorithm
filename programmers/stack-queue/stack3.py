def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        if i == ")":
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return True


answer = "(())()"
answer2 = "(()("

print(solution(answer2))