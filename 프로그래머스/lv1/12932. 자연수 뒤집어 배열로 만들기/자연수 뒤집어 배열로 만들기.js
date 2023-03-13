function solution(n) {
    var answer = [];
    var tmp = String(n).split('').reverse();
    for (t of tmp) {
        answer.push(Number(t))
    }
    return answer;
}