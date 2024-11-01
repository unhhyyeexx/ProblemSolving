function solution(n, times) {
    times.sort((a, b) => a - b);
    let left = 1, right = times[times.length - 1] * n;
    let answer = right;
    
    while (left <= right) {
        // 초기 left와 right는 걸리는 시간의 최소값과 최대값
        // 이분탐색을 통해 넘치지도, 부족하지도 않은 시간을 찾아간다.
        const mid = Math.floor((left + right) / 2); // 현재 비교할 시간
        let done = 0; // 심사한 사람의 수
        for (time of times) {
            // 해당 심사대에서 주어진 시간동안 심사 받은 사람 수 더하기
            done += Math.floor(mid / time);
            if (done >= n) break
        }
        if (done >= n) {
            // 심사받을 사람보다 많은 사람을 심사할 시간이 된다면
            // 시간을 줄이기 위해 right를 mid의 앞으로 가져온다.
            right = mid - 1;
            answer = mid
        } else left = mid + 1;
    }
    return answer;
}