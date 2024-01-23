def plus_ascii(char):
    result = 0
    while char != 'A':
        ascii_value = ord(char)
        if ascii_value + 1 > ord('Z'):
            ascii_value = ord('A') - 1
        char = chr(ascii_value + 1)
        result += 1
    return result

def minus_ascii(char):
    result = 0
    while char != 'A':
        ascii_value = ord(char)
        if ascii_value - 1 < ord('A'):
            ascii_value = ord('Z') + 1
        char = chr(ascii_value - 1)
        result += 1
    return result

def find_left_right(name):
    left, right = 0, 0
    is_right = True
    for i in range(len(name)):
        if name[i] == 'A':
            break
        else:
            right += 1
    for i in range(len(name)-1, -1, -1):
        if name[(i + 1) % len(name)] == 'A':
            break
        else:
            left += 1
    if left < right:
        is_right = False
    return is_right
        
def solution(name):
    answer = 0
    now = 0
    len_name = len(name)
    for i in range(len_name):
        char = name[i]
        if char == 'A':
            continue
        else:
            left_or_right = min(i - now, now - (i - len_name))
            answer += left_or_right
            now = i
        up_or_down = min(plus_ascii(char), minus_ascii(char))
        answer += up_or_down
    return answer

def another_solution(name):
    
    # 알파벳 변경 횟수( 상하 이동 ) 
    spell_move = 0
    # 커서 이동 횟수, 이름의 길이 - 1( 좌우 이동 )
    cursor_move = len(name) - 1  
    
    for i, spell in enumerate(name):
    	# 알파벳 변경 횟수, 위아래 중 최소 이동 값 ( 상하 이동 )
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        
    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )    
    return spell_move + cursor_move

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23

print(solution("BBAAAAAAB")) # 6
print(solution("BBAAAAABB")) # 8
print(solution("AABBAABA"))