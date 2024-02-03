import sys

n, m = map(int, sys.stdin.readline().split())

d_key = {}
d_value = {}

for i in range(n):
    value = sys.stdin.readline()
    d_key[i + 1] = value
    d_value[value] = i + 1
    
for _ in range(m):
    user_input = sys.stdin.readline()
    try:
        int_value = int(user_input)
        print(d_key[int_value], end="")
    except:
        print(d_value[user_input])