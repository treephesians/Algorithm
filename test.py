def solution(N, number):
    if N == number:
        return 1
    
    # dp 리스트 초기화. dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    print(dp)
    dp[1].add(N)

    for i in range(2, 9):
        # N을 i번 연속해서 붙인 숫자를 추가 (예: 55, 555)
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    # 사칙연산 적용
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
            
            # number를 찾으면 바로 반환
            if number in dp[i]:
                return i
    
    return -1  # 8번 이내에 찾지 못한 경우

# 예시 테스트
print(solution(5, 12))  # 4 반환 예시
print(solution(2, 11))  # 3 반환 예시 (2+2+2*2+2/2)