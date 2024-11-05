function solution(n, lost, reserve) {
    let answer = n - lost.length;
    lost.sort((a, b) => a-b);
    const visit = Array.from({length: n+1}, ()=>(0));
    for (let i=0; i<n; i++) {
        const tmp = lost[i]
        if (reserve.includes(lost[i])) {
            visit[i] = 1;
            answer += 1;
        } else{
            if (reserve.includes(tmp-1) && !lost.includes(tmp-1) && visit[tmp-1] === 0) {
                visit[tmp-1] = 1;
                answer += 1;
            } else if (reserve.includes(tmp+1) && !lost.includes(tmp+1) && visit[tmp+1] === 0) {
                visit[tmp+1] = 1;
                answer += 1;
            }
        }
    }
    return answer;
}