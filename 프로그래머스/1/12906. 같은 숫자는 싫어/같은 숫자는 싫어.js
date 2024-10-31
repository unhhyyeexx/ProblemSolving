function solution(arr){
    var answer = [];
    tmp = arr[0]
    for (let i=1; i<arr.length; i++) {
        if (tmp === arr[i]) continue;
        answer.push(tmp)
        tmp = arr[i]
    }
    answer.push(tmp)

    return answer;
}