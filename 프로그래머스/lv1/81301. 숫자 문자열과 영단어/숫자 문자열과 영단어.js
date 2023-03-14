function solution(s) {
    var answer ='';
    var stack = []
    var nums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6','seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'};
    for (i of s) {
        if (Object.keys(nums).includes(stack.join(''))) {
            answer += nums[stack.join('')]
            stack = []
        } 
        if (isNaN(i)) stack.push(i)
        else {
            answer += i
        }
    }
    if (stack.length > 0) {
        answer += nums[stack.join('')]
    }
    return Number(answer);
}