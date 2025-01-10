import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

# 각 카드의 점수 초기화
scores = {card: 0 for card in cards}

# 카드 정렬
cards_sorted = sorted(cards)
cards_set = set(cards)  # 빠른 탐색을 위해 set 생성

# 카드별 점수 계산 (배수 관계 탐색)
for x in cards_sorted:
    multiple = x * 2
    while multiple <= cards_sorted[-1]:
        if multiple in cards_set:  # set에서 O(1)로 탐색
            scores[x] += 1  # x가 승리
            scores[multiple] -= 1  # multiple이 패배
        multiple += x

# 결과 출력
print(" ".join(map(str, [scores[card] for card in cards])))