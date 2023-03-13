function solution(arr)
{
    var answer = [];
    var stack = [];
    for (a of arr) {
        if(stack.length===0){
            stack.push(a);
        } else if (stack[0] === a) {
            continue;
        } else {
            answer.push(stack.pop())
            stack.push(a)
        }
    }
    if (stack.length) answer.push(stack.pop())

    return answer;
}