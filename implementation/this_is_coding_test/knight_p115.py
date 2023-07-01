data = input()

alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x= data[0]
x = alpha[x]
y = int(data[1])
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
count = 0
for i in range(1,8+1):
    _x = x + dx[i - 1]
    _y = y + dy[i - 1]
    if _x >= 1 and _x <= 8 and _y >= 1 and _y <= 8:
        count += 1
print(count)