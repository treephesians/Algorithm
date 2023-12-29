def solution(answers):
    answer = []
    score = [0,0,0]
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == answer1[i % len(answer1)]:
            score[0] += 1
        if answers[i] == answer2[i % len(answer2)]:
            score[1] += 1
        if answers[i] == answer3[i % len(answer3)]:
            score[2] += 1
    
    max_score = max(score)
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)

    return answer

answers = [1,3,2,4,2]
answers = [1,2,3,4,5]
print(solution(answers))
