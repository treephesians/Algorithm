arr = input().split('-')
result = 0
for i in range(len(arr)):
    arr2 = arr[i].split('+')
    for j in arr2:
        if i == 0:
            result += int(j)
        else:
            result -= int(j)
print(result)