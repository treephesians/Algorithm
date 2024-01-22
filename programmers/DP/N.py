def solution(N, number):
    numbers = [set() for _ in range(9)]
    for i in range(1,9):
        numbers[i].add(int(str(N)*i))
        for j in range(1, i // 2 + 1):
            for n in numbers[j]:
                for m in numbers[i - j]:
                    numbers[i].add(n + m)
                    numbers[i].add(n - m)
                    numbers[i].add(n * m)
                    numbers[i].add(m - n)
                    if n != 0:
                        numbers[i].add(m // n)
                    if m != 0:
                        numbers[i].add(n // m)
        
        if number in numbers[i]:
            return i
    return -1

print(solution(5, 12)) # answer  4
print(solution(2, 11)) # answer 3