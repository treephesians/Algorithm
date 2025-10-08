from itertools import combinations, product

def solution(dice):
    n = len(dice)
    half = n // 2
    dice_idx = list(range(n))
    
    max_win = -1
    best_choice = []
    
    for a_choice in combinations(dice_idx, half):
        # B의 주사위
        b_choice = [i for i in dice_idx if i not in a_choice]
        
        # A, B 주사위 조합
        a_dice = [dice[i] for i in a_choice]
        b_dice = [dice[i] for i in b_choice]
        
        win_count = 0
        # 모든 주사위 굴림 경우
        for a_roll in product(*a_dice):
            for b_roll in product(*b_dice):
                if sum(a_roll) > sum(b_roll):
                    win_count += 1
        
        if win_count > max_win:
            max_win = win_count
            best_choice = sorted([i + 1 for i in a_choice])  # 1번 주사위 기준
    
    return best_choice