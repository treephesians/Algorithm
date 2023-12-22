def my_solution(citations):
    
    answer = 0
    for i in range(max(citations)+1):
        num = 0
        for j in citations:
            if j >= i:
                num += 1
        if num >= i:
            answer = i
    return answer

def solution(citations):
    citations.sort(reverse=True)
    l = map(min, enumerate(citations, start=1))
    #l = enumerate(citations, start=1)
    print(list(enumerate(citations, start=1)))
    print(list(l))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
            
        
        

citations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
citations = [3, 0, 6, 1, 5]
#citations = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#citations = [999, 1000]
#            0  1  2  3  4   5   6   7   8   9
print(solution(citations))