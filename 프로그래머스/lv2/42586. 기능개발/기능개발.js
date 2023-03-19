function solution(progresses, speeds) {
    var answer = [];
    var q = [];
    var cnt = 0;
    for (let i=0; i<progresses.length; i++) {
        var tmp = Math.ceil((100-progresses[i])/speeds[i]);
        
        if (q.length === 0) q.push(tmp);
        else {
            if (q[0] < tmp) {
                while (q.length > 0){
                    q.shift();
                    cnt++;
                }
                answer.push(cnt);
                cnt = 0;
            }
            q.push(tmp);
        }
    }
    if (q.length > 0) {
        while (q.length > 0) {
            q.shift();
            cnt++;
        }
        answer.push(cnt);
    }
    return answer;
}