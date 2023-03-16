function solution(begin, target, words) {
    var answer = 0;
    var n = begin.length, m = words.length;
    
    function check(begin, word) {
        var tmp = 0;
        for (let i=0; i<n; i++){
            if (begin[i] !== word[i]) tmp++;
        }
        return tmp === 1 ? true : false;
    }
    
    var q = [], visit = new Array(m).fill(false);
    q.push([begin, 0]);
    
    while (q.length > 0) {      
        var [now, cnt] = q.shift();
        if (now === target) return cnt;
        for ([idx, word] of words.entries()) {
           if (!visit[idx] && check(now, word)) {
               q.push([word, cnt+1]);
               visit[idx] = true;
           }
        }
    }
    return answer;
}