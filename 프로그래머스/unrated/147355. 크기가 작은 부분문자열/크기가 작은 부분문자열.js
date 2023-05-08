function solution(t, p) {
    var answer = 0;
    var n = p.length;
    for (let i=0; i<(t.length - n + 1); i++) {
        if (parseInt(t.slice(i, i+n)) <= parseInt(p)) {
            answer += 1
        }
    }
    return answer;
}