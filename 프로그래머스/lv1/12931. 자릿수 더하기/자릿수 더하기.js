function solution(n)
{
    var answer = 0;
    n = String(n);
    for (var i of n) {
        answer += Number(i)
    }

    return answer;
}