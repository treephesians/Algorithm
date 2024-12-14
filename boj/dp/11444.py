# https://www.acmicpc.net/problem/11444
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def mat_mul(A, B):
    # 2x2 행렬 곱셈
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(M, n):
    # M^n을 분할정복으로 계산
    # n=0일 때 단위행렬 반환
    result = [[1,0],[0,1]]
    base = M
    while n > 0:
        if n % 2 == 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        n //= 2
    return result

n = int(input())
if n == 0:
    print(0)
else:
    M = [[1,1],[1,0]]
    Mn = mat_pow(M, n)
    # M^n = [[F_{n+1}, F_n],[F_n, F_{n-1}]] 이므로 F_n = Mn[0][1] 또는 Mn[1][0]
    print(Mn[0][1] % MOD)