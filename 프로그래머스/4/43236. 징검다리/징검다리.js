function solution(distance, rocks, n) {
    var answer = 0;
    rocks.push(distance);
    rocks.sort((a, b) => a-b);
    
    let left = 0, right = distance;
    while (left<=right) {
        const mid = Math.floor((left+right)/2); // 임의의 거리의 최솟값, 이것보다 작으면 돌 삭제
        let current = 0, removeCnt = 0; // 현재위치, 지운 돌 개수
        let minDistance = distance;
        
        for (rock of rocks) {
            let diff = rock - current;
            if (diff < mid) removeCnt += 1;
            else {
                current = rock;
                minDistance = Math.min(minDistance, diff);
            }
        }
        // 지워야 하는 돌보다 더 많이 지웠다면,
        // 설정한 임의의 최소거리 mid가 너무 큰 값, 범위를 좁혀서 돌을 덜 지우게 만든다.
        // n만큼 돌을 지웠거나, 덜 지웠다면,
        // 최솟값들 중 최댓값을 찾아야 함. 일단 정답을 저장한 뒤 left를 증가시켜 범위를 넓힌 다음, 최솟값에서 만족하지 않고 반대 방향으로 탐색해 최솟값들 중 최댓값을 찾는다.
        if (removeCnt > n) right = mid - 1;
        else {
            answer = minDistance;
            left = mid + 1;
        }
    }
    return answer;
}