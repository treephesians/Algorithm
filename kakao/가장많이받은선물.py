def solution(friends, gifts):
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    friend_ids = {v : i for i, v in enumerate(friends)}
    result = [{"give" : 0, "get" : 0, "predict" : 0} for _ in range(len(friends))]

    for gift in gifts:
        sender, to = gift.split(" ")
        arr[friend_ids[sender]][friend_ids[to]] += 1
        result[friend_ids[sender]]["give"] += 1
        result[friend_ids[to]]["get"] += 1

    for row in range(len(friends)):
        for col in range(row + 1, len(friends)):
            if arr[row][col] > arr[col][row]:
                result[row]["predict"] += 1
            elif arr[row][col] < arr[col][row]:
                result[col]["predict"] += 1
            elif result[row]["give"] - result[row]["get"] < result[col]["give"] - result[col]["get"]:
                result[col]["predict"] += 1
            elif result[row]["give"] - result[row]["get"] > result[col]["give"] - result[col]["get"]:
                result[row]["predict"] += 1
        
    return max(x["predict"] for x in result)

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends, gifts))