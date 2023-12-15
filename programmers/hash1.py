def solution(participant, completion):
    answer = {}

    for player in participant:
        if player in answer.keys():
            answer[player] += 1
        else:
            answer[player] = 1

    for player in completion:
        if player in answer.keys():
            answer[player] -=1

    for key, value in answer.items():
        if value >= 1:
            return key
    return 0


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))