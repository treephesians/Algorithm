import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [0 * (K + 1)]
for _ in range(N):
    W, V = map(int, input().split())
    arr[W] = max(arr[W], V)


'''
6 6
4 8
3 6
2 5
1 2
5 6
'''
    