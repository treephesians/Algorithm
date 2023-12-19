import time



def solution1(participant, completion):
    answer = ""
    for player in participant:
        if player not in completion:
            answer = player
        else:
            completion.remove(player)
    return answer


def solution2(participant, completion):
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

# Worst Case
w_participant = [str(i) for i in range(100000)]
w_completion = [str(i) for i in range(100000 - 1)]

# Best Case
b_participant = ["1" for i in range(100000)]
b_completion = ["1" for i in range(100000 - 1)]

start_time = time.time()
solution1(w_participant, w_completion)
end_time = time.time()
print(f"code1 worst time : {end_time - start_time}")

start_time = time.time()
solution1(b_participant, b_completion)
end_time = time.time()
print(f"code1 best time : {end_time - start_time}")

start_time = time.time()
solution2(w_participant, w_completion)
end_time = time.time()
print(f"code2 worst time : {end_time - start_time}")

start_time = time.time()
solution2(b_participant, b_completion)
end_time = time.time()
print(f"code2 best time : {end_time - start_time}")
