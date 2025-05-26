import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for t in range(T):
    p = input()
    len_arr = int(input())
    arr = eval(input())
    dq = deque(arr)

    reversed_flag = False
    result = True

    for i in range(len(p)):
        if p[i] == 'R':
            reversed_flag = not reversed_flag
        elif p[i] == 'D':
            if len(dq) < 1:
                result = False
                break
            if not reversed_flag:
                dq.popleft()
            elif reversed_flag:
                dq.pop()

    if not result:
        print("error")
    else:
        ldq = list(dq)
        if reversed_flag:
            ldq.reverse()
        print(ldq)





# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []