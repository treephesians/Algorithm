import sys
import math

sys.setrecursionlimit(10000)

def Z(x, y, size):
    half_size = size // 2
    position = int(math.pow(half_size, 2))
    if 0 <= x < half_size and 0 <= y < half_size:
        if size == 2:
            return 0
        else:
            return position * 0 + Z(x, y, half_size)
    elif half_size <= x < size and 0 <= y < half_size:
        if size == 2:
            return 1
        else:
            return position * 1 + Z(x % half_size, y, half_size)
    elif 0 <= x < half_size and half_size <= y < size:
        if size == 2:
            return 2
        else:
            return position * 2 + Z(x, y % half_size, half_size)
    elif half_size <= x < size and half_size <= y < size:
        if size == 2:
            return 3
        else:
            return position * 3 + Z(x % half_size, y % half_size, half_size)
        
    
n, r, c = map(int, sys.stdin.readline().split())
answer = Z(c, r, int(math.pow(2, n)))
print(answer)