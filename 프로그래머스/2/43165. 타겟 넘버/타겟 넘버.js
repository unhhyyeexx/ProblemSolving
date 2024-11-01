function solution(numbers, target) {
    var answer = 0;
    
    function dfs(sumValue, depth){
        if (depth === numbers.length) {
            if (sumValue === target) answer++;
            return;
        };
        dfs(sumValue + numbers[depth], depth+1);
        dfs(sumValue - numbers[depth], depth+1);    
    }
    
    dfs(0, 0)
    return answer;
}