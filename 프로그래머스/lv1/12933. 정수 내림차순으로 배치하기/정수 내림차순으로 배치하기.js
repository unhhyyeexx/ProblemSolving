function solution(n) {
    var answer = 0;
    n = String(n).split("")
    n.sort((a, b) => Number(b)-Number(a))
    answer = Number(n.join(""))
    return answer;
}