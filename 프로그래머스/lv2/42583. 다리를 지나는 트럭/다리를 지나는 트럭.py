from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    tmp = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    
    while bridge:
        answer += 1
        tmp -= bridge[0]
        bridge.popleft()
        if truck_weights:
            if tmp + truck_weights[0] <= weight:
                tmp += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer