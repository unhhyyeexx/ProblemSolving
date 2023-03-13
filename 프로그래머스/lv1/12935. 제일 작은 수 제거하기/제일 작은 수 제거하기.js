function solution(arr) {
    if (arr.length === 1) {
        return [-1]
    }
    var idx = arr.indexOf([...arr].sort((a, b)=>a-b)[0]);
    arr.splice(idx, 1)
    return arr
}