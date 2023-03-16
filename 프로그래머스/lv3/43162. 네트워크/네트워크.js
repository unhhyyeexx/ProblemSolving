function solution(n, computers) {
    var answer = 0;
    var visit = new Array(n).fill(false);
    
    function dfs(idx) {
        visit[idx] = true;
        for (let i=0; i<n; i++) {
            if(computers[idx][i] && !visit[i]){
                dfs(i);
            }
        }
    }
    
    for (let k=0; k<n; k++){
        if (!visit[k]){
            dfs(k);
            answer++;
        }
    }
    return answer;
}