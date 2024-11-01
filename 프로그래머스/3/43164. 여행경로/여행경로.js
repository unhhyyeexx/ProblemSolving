function solution(tickets) {
    let answer = [];
    let graph = {};
    tickets.forEach((el, idx) =>{
        let s = el[0], e = el[1]
        if (graph[s]) graph[s].push([e, idx]);
        else graph[s] = [[e, idx]];
    })
    let n = tickets.length;
    let visit = Array.from(Array(n), ()=>(0));
    
    function dfs(now, path){
        if (path.length === n + 1) {
            answer.push(path)
            return
        }
        if (graph[now]){
            graph[now].forEach((el, idx) =>{
                let end = el[0], i = el[1]
                if(visit[i] === 0) {
                    visit[i] = 1;
                    dfs(end, [...path, end]);
                    visit[i] = 0;
            }
        })
            
        }
            
    }
    
    dfs("ICN", ["ICN"]);
    answer.sort()
    return answer[0];
}