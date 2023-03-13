function solution(arr1, arr2) {
    var answer = [];
    for (i in arr1) {
        var tmp = []
        for (j in arr1[i]) {
            tmp.push(arr1[i][j] + arr2[i][j])
        }
        answer.push(tmp)
    }
    return answer;
}