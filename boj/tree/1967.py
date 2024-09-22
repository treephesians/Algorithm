import sys

def find_max_len_v(n, start, tree):
    stack = [[start,0]]
    visited = [False] * (n + 1)
    max_len = 0
    max_v = start
    while stack:
        v = stack.pop()[0]
        w = stack.pop()[1]
        visited[v] = True
        if len(tree[v]) > 1:
            for i in range(len(tree[v])):
                next_v = tree[v][i][0]
                next_w = tree[v][i][1]
                if not visited[next_v]:
                    stack.append([next_v, w + next_w])
        else:
            if max_len < w:
                max_len = w
                max_v = v
    return max_v


n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append([c, w])
    tree[c].append([p, w])

v = find_max_len_v(n, 1, tree)
print(v)
