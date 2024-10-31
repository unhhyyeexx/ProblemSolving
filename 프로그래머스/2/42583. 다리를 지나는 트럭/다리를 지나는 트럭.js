function solution(bridge_length, weight, truck_weights) {
    // q=[트럭무게, 이 트럭이 나갈 시간]
    let time = 0, q = [[0,0]], weightOnBridge = 0;
    
    while (q.length > 0 || truck_weights.length > 0) {
        // 현재 시간이 맨 앞 트럭이 나갈 시간과 같으면 내보내고 무게 합 뺌
        if (q[0][1] == time) weightOnBridge -= q.shift()[0];
        if (weightOnBridge + truck_weights[0] <= weight) {
             // 다리에 새 트럭이 올라올 수 있는 상황
            weightOnBridge += truck_weights[0];
            q.push([truck_weights.shift(), time+bridge_length]);
        } else{ 
            // 다리에 새 트럭이 못올라오는 상황이면
            // 첫 트럭 빠지도록 그 시간으로 점프
            if (q[0]) time = q[0][1] - 1;
        }
        time++;
    }
    
    return time;
}