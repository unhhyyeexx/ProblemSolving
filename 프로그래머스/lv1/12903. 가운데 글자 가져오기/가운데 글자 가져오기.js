function solution(s) {
    var answer = '';
    var len = s.length
    if (len % 2 === 0) {
        answer += s.slice(len/2-1, len/2+1)
    } else {
        answer += s[parseInt(len/2)]
    }
    return answer;
}