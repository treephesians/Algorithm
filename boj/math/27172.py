import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

# 각 카드의 점수 초기화
scores = {card:0 for card in cards}

# 카드 정렬
cards_sorted = sorted(cards)

# 카드별 점수 계산 (배수 관계 탐색)
max_card = cards_sorted[-1]

for i in range(N):
    x = cards_sorted[i]
    multiple = x * 2
    while multiple <= max_card:
        # 배수 관계에 해당하는 카드의 점수 조정
        if multiple in cards:
            scores[x] += 1  # x가 승리
            scores[multiple] -= 1  # multiple이 패배
        multiple += x

# 결과 출력
print(" ".join(map(str, scores.values())))