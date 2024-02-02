memory = [[0,1],[1,0]]

t = int(input())
for i in range(t):
    n = int(input())
    l = len(memory)
    if n >= l:
        for j in range(n - l + 1):
            nl = len(memory)
            new = [memory[nl - 1][0] + memory[nl- 2][0], memory[nl - 1][1] + memory[nl- 2][1]]
            memory.append(new)
    print(str(memory[n][1]) + " " + str(memory[n][0]))
            
    