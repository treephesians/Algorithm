import sys

A, B, C = map(int, sys.stdin.readline().split())

def f(A, B, C):
     if B == 1:
          return A % C
     elif B % 2 == 0:
          return (f(A, int(B // 2), C) ** 2) % C
     else:
          return ((f(A, int(B // 2), C) ** 2) * A) % C

print(f(A, B, C))