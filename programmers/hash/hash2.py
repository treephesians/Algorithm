import collections

def solution(nums):
    l = len(nums)
    arr = dict(collections.Counter(nums))
    answer = min(l/2, len(arr.keys()))
    return answer

nums = [3,3,3,2,2,2]

r = solution(nums)
print(r)