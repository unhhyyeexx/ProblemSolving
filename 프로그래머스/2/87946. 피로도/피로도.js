

function solution(k, dungeons) {
    var answer = 0;
    const n = dungeons.length;
    const visit = Array.from({length: n}, ()=> 0);
    
    function dfs(k, cnt) {
        answer = Math.max(answer, cnt);
    
        dungeons.forEach((el, idx) => {
            if (visit[idx] === 0 && k >= el[0]){
                visit[idx] = 1;
                dfs(k-el[1], cnt + 1);
                visit[idx] = 0;
            }
        })
    }
    dfs(k, 0);
    
    return answer;
}