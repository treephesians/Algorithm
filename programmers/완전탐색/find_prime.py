from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
        
    combinations = set()  # 중복을 피하기 위해 집합을 사용

    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            number = int(''.join(p))
            combinations.add(number)

    for number in sorted(combinations):
        if isPrime(number):
            answer += 1
        
    return answer

numbers = "011"
print(solution(numbers))