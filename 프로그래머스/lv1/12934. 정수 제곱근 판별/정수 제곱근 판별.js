function solution(n) {
    var x = Math.sqrt(n)
    if (x % 1 === 0) {
        return Math.pow(x+1, 2)
    } else {
        return -1
    }
}