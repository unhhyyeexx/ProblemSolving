function solution(s){
    var answer = true;

    s = s.toUpperCase()
    var pcnt = [...s].filter(x => x === 'P').length
    var ycnt = [...s].filter(x => x === 'Y').length
    
    if (pcnt !== ycnt) {
        answer = false
    }
    
    return answer;
}