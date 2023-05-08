function solution(x) {
    var answer = true;
    var tmp = x.toString();
    var divnum = 0;
    for (let i=0; i<tmp.length; i++) {
        divnum += parseInt(tmp[i]);
    }
    if (x % divnum !== 0) {
        answer = false
    }
    return answer;
}