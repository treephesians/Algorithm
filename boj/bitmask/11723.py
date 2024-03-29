import sys

M = int(sys.stdin.readline())

S = set([])

for _ in range(M):
    line = sys.stdin.readline().split()
    func = line[0]
    
    if len(line) > 1:
        n = int(line[1])
        
    if func == "add":
        S.add(n)
    
    elif func == "remove":
        if n in S:
            S.remove(n)
    
    elif func == "check":
        if n in S:
            print(1)
        else:
            print(0)
    
    elif func == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    
    elif func == "all":
        S = set([i for i in range(1, 21)])
    
    elif func == "empty":
        S = set([])