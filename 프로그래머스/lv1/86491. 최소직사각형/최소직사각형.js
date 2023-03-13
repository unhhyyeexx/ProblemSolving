function solution(sizes) {
    var answer = 0;
    var w = [];
    var h = [];
    for (size of sizes) {
        w.push(Math.max(...size));
        h.push(Math.min(...size));
    }
    console.log(w, h)
    answer = Math.max(...w) * Math.max(...h);
    
    return answer;
}