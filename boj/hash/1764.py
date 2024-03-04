import sys

N, M = map(int, sys.stdin.readline().split())
my_dict = {}
for _ in range(N):
    name = sys.stdin.readline()
    my_dict[name] = 1

for _ in range(M):
    name = sys.stdin.readline()
    if name in my_dict:
        my_dict[name] += 1
        
keys_with_value_2 = [key for key, value in my_dict.items() if value == 2]
keys_with_value_2.sort()

print(len(keys_with_value_2))
for key in keys_with_value_2:
    print(key, end="")