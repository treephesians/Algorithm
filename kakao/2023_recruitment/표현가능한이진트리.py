def make_binary(num):
    arr = []
    while num:
        arr.append(num % 2)
        num //= 2
    count = 1
    while count <= len(arr):
        count *= 2
    while len(arr) < count - 1:
        arr.append(0)
    arr.reverse()
    print(arr)
    return arr

def check(arr, start, end):
    if start == end:
        return True
    mid_index = (start + end) // 2
    if arr[mid_index] == 0 and (1 in arr[start : mid_index] or 1 in arr[mid_index + 1 : end]):
        return False
    return check(arr, start, mid_index) and check(arr, mid_index + 1, end)


def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        binary_arr = make_binary(numbers[i])
        answer[i] = 1 if check(binary_arr, 0, len(binary_arr)) else 0

    return answer

print(solution(numbers=[2]))
# 010