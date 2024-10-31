function solution(progresses, speeds) {
    var answer = [];
    var day = null;
    var cnt = 0
    for (let i=0; i<progresses.length; i++) {
        let tmp = (100-progresses[i])%speeds[i] ? parseInt((100-progresses[i])/speeds[i])+1 : parseInt((100-progresses[i])/speeds[i])
        if (!day) {
            day = tmp
            cnt += 1
        } else if (day < tmp) {
            day = tmp
            answer.push(cnt)
            cnt = 1
        } else{
            cnt += 1
        }
    }
    if (cnt > 0) answer.push(cnt)
    return answer;
}