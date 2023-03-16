function solution(numbers, target) {
    var answer = 0;
    var n = numbers.length;
    
    function dfs(count, sum) {
        if (count === n) {
            if (target === sum) {
                answer ++;
            }
            return;
        }
        dfs(count+1, sum+numbers[count]);
        dfs(count+1, sum-numbers[count]);
    }
    
    dfs(0,0);
    
    return answer;
}