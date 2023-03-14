function solution(N, stages) {
    var answer = [];
    var people = stages.length
    var cnt = new Array(N+2).fill(0);
    for (stage of stages){
        cnt[stage] += 1
    }
    var fail = []
    for (let i=1; i<N+1; i++) {
        f = cnt[i]
        if (f === 0) fail.push(0)
        else{
            fail.push(f/people)
            people -= f
        }
    }
    var tmp = [...fail].sort().reverse();
    for (i in tmp) {
        idx = fail.indexOf(tmp[i])
        answer.push(idx+1)
        delete fail[idx]
    }
    return answer;
}