def f():
    a, b = map(int, input().split(' '))
    n = 1
    while a < b:
        n += 1
        if b % 2 == 0:
            b = b // 2
        elif b % 10 == 1:
            b = b // 10
        else:
            return -1
        if a == b:
            return n
    return -1

print(f())