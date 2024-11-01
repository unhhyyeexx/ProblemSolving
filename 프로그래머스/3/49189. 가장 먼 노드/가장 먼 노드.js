function solution(n, edge) {
    var answer = 0;
    let visit = Array.from(Array(n+1), ()=>(0));
    let graph = Array.from(Array(n+1), ()=>(Array()));
    
    for ([s, e] of edge) {
        graph[s].push(e);
        graph[e].push(s);
    }
    q = [1];
    visit[1] = 1;
    while (q.length > 0) {
        let now = q.shift();
        if (graph[now]){
            graph[now].forEach((el) => {
                if (visit[el] === 0) {
                    visit[el] = visit[now] + 1;
                    q.push(el);
                };
            });
        }
    }

    let maxValue = Math.max(...visit)
    answer = visit.reduce((cnt, el) => cnt + (maxValue===el), 0);
    
    return answer;
}