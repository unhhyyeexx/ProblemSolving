function solution(nums) {
    var answer = 0;
    var setnums = new Set(nums);
    if (setnums.size < nums.length / 2) {
        return setnums.size
    } else {
        return nums.length / 2
    }
}