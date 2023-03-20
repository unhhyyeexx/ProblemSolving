function solution(s){
    var answer = true;
    var stack = [];
    
    for (b of s) {
        if (stack.length === 0) {
            if (b === ")") return false
            stack.push(b);
        } else {
            if (b === "(") stack.push(b);
            else {
                if (stack[stack.length-1] === ')') return false
                else stack.pop()
            }
        }
    }
    if (stack.length) return false;
    
    return answer;
}