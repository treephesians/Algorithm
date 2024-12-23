import sys

N = int(sys.stdin.readline().strip())

def count_digits(n, counts):
    # n까지의 숫자에서 각 자릿수를 pos를 기준으로 세기
    pos = 1
    while pos <= n:
        # ex) n=258, pos=1(1의자리)일 때
        # higher=25, current=8, lower=0
        # pos=10(10의자리)일 때
        # higher=2, current=5, lower=8
        # pos=100(100의자리)일 때
        # higher=0, current=2, lower=58
        higher = n // (pos * 10)
        current = (n // pos) % 10
        lower = n % pos
        
        # 0~9까지 각 숫자에 대해 처리
        for digit in range(10):
            # 기본적으로 higher * pos 만큼 digit이 나타난다.
            counts[digit] += higher * pos
        
        # current 숫자를 기준으로 처리
        for digit in range(current):
            counts[digit] += pos
        
        # 현재 자릿수에 해당하는 digit이 current인 경우 lower+1 만큼 더해준다.
        counts[current] += lower + 1
        
        # 0의 경우 맨 앞에 오는 경우는 제외해야 한다.
        # pos*10보다 큰 higher 부분에서 leading zero가 카운트된 것을 빼준다.
        counts[0] -= pos
        pos *= 10

counts = [0]*10
count_digits(N, counts)

print(' '.join(map(str, counts)))