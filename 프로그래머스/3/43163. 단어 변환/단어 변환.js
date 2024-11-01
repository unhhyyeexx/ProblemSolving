function solution(begin, target, words) {
    
    let cnt = begin.length;
    let n = words.length;
    let visit = Array.from(Array(n), ()=>(0));
    
    function check(now, word) {
        // now는 현재 단어, word는 비교할 단어
        // now와 word가 한 글자 다른 단어면 true, 아니면 false 반환
        let checkCnt = 0; // 같은 글자 세기
        for (let w=0; w<cnt; w++) {
            // 한글자씩 비교해서 한 글자 같으면 checkCnt += 1
            if (word[w] === now[w]) checkCnt++;
        }
        if (checkCnt === (cnt -1)) return true;
        
        return false;
    }
    
    q = [[begin, 0]];
    
    while (q.length > 0){
        let[now, dep] = q.shift();
        if (now === target) return dep;
        for (let i=0; i<n; i++){
            if (visit[i] === 0 && check(now, words[i])) {
                visit[i] = 1;
                q.push([words[i], dep+1]);
            }
        }   
    }
    
    return 0;
}