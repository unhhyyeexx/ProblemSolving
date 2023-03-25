function solution(order) {
    var answer = 0;
    var assist = [];
    var i = 1;
    while (i <= order.length) {
        assist.push(i);
        while (assist.length>0 && assist[assist.length-1]===order[answer]){
            answer += 1;
            assist.pop();
        }
        i+=1;
    }
    return answer;
}