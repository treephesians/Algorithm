import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

s = sorted(set(arr))

dic = {}

for i in range(len(s)):
    dic[s[i]] = i

for i in range(N):
    print(dic[arr[i]], end=" ")