def my_sum(arr):

    result = 0

    for i in arr:
        result += i[0]
    
    return result
        


def solution(bridge_length, weight, truck_weights):
    answer = 0

    on_bridge = []
    i = 0

    while(truck_weights):

        for truck in on_bridge:
            truck[1] += 1

        for truck in on_bridge:
            if truck[1] >= bridge_length:
                on_bridge.remove(truck)

        if len(on_bridge) < bridge_length and my_sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append([truck_weights[0], 0])
            truck_weights.remove(truck_weights[0])

        answer += 1
    
    while(on_bridge):
        for truck in on_bridge:
            truck[1] += 1

        for truck in on_bridge:
            if truck[1] >= bridge_length:
                on_bridge.remove(truck)
        answer += 1
            

    return answer

bl = 2
w = 10
tw = [7,4,5,6]

print(solution(bl, w, tw))