# 2
# 3
# hat headgear
# sunglasses eyewear
# turban headgear
# 3
# mask face
# sunglasses face
# makeup face

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    D = defaultdict(int)
    
    for n in range(N):
        name, category = input().split()
        D[category] += 1

    result = 1
    for i in D.values():
        result *= i + 1
        
    print(result - 1)
    
    
        