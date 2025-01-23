'''
1 2 3
4 5 6
7 8 9
* 0 #

위와 같은 모양으로 배열된 숫자 자판이 있습니다. 숫자 타자 대회는 이 동일한 자판을 사용하여 숫자로만 이루어진 긴 문자열을 누가 가장 빠르게 타이핑하는지 겨루는 대회입니다.

대회에 참가하려는 민희는 두 엄지 손가락을 이용하여 타이핑을 합니다. 민희는 항상 왼손 엄지를 4 위에, 오른손 엄지를 6 위에 두고 타이핑을 시작합니다. 엄지 손가락을 움직여 다음 숫자를 누르는 데에는 일정 시간이 듭니다. 민희는 어떤 두 숫자를 연속으로 입력하는 시간 비용을 몇몇 가중치로 분류하였습니다.

이동하지 않고 제자리에서 다시 누르는 것은 가중치가 1입니다.
상하좌우로 인접한 숫자로 이동하여 누르는 것은 가중치가 2입니다.
대각선으로 인접한 숫자로 이동하여 누르는 것은 가중치가 3입니다.
같지 않고 인접하지 않은 숫자를 누를 때는 위 규칙에 따라 가중치 합이 최소가 되는 경로를 따릅니다.
예를 들어 1 위에 있던 손가락을 0 으로 이동하여 누르는 것은 2 + 2 + 3 = 7 만큼의 가중치를 갖습니다.
단, 숫자 자판은 버튼의 크기가 작기 때문에 같은 숫자 버튼 위에 동시에 두 엄지 손가락을 올려놓을 수 없습니다. 즉, 어떤 숫자를 눌러야 할 차례에 그 숫자 위에 올려져 있는 손가락이 있다면 반드시 그 손가락으로 눌러야 합니다.

숫자로 이루어진 문자열 numbers가 주어졌을 때 최소한의 시간으로 타이핑을 하는 경우의 가중치 합을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ numbers의 길이 ≤ 100,000
numbers는 아라비아 숫자로만 이루어진 문자열입니다.

입출력 예
numbers	result
"1756"	10
"5123"	8
'''

from collections import defaultdict

def solution(numbers):
    # 숫자 자판의 좌표 매핑
    keypad = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '*': (3, 0), '0': (3, 1), '#': (3, 2),
    }
    
    def move_cost(pos1, pos2):
        if pos1 == pos2:
            return 1  # 제자리
        x1, y1 = pos1
        x2, y2 = pos2
        dx, dy = abs(x1 - x2), abs(y1 - y2)
        if dx + dy == 1:  # 상하좌우 인접
            return 2
        elif dx == 1 and dy == 1:  # 대각선 인접
            return 3
        else:
            # 대각선 최대 사용 + 나머지 상하좌우 이동
            return 3 * min(dx, dy) + 2 * abs(dx - dy)

    # DP 테이블: {왼손 위치, 오른손 위치} -> 최소 비용
    dp = defaultdict(lambda: float('inf'))
    dp[(4, 6)] = 0  # 초기: 왼손 4, 오른손 6 위치

    # 숫자 입력 처리
    for num in numbers:
        num_pos = keypad[num]
        new_dp = defaultdict(lambda: float('inf'))
        
        for (left, right), cost in dp.items():
            left_pos, right_pos = keypad[str(left)], keypad[str(right)]
            
            # 왼손으로 num을 누르는 경우
            if right != num:  # 같은 숫자에 두 손가락이 갈 수 없음
                new_dp[(num, right)] = min(new_dp[(num, right)], cost + move_cost(left_pos, num_pos))
            
            # 오른손으로 num을 누르는 경우
            if left != num:
                new_dp[(left, num)] = min(new_dp[(left, num)], cost + move_cost(right_pos, num_pos))
        
        dp = new_dp

    # 최종 최소 비용
    return min(dp.values())

# 예제 입력
print(solution("1756"))  # 10
print(solution("5123"))  # 8