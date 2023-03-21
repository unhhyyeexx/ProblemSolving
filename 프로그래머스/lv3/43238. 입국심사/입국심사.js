function solution(n, times) {
    times.sort((a,b)=> a-b);
    var left = 1;
    var right = n*times[times.length - 1];
    var answer = right;
    
    while (left <= right) {
        var mid = Math.floor((left+right)/2);
        var cnt = 0;
        for (time of times) {
            cnt += Math.floor(mid/time);
            if (cnt >= n) {
                answer = Math.min(mid, answer);
            }
        }
        if (cnt>=n) right = mid-1;
        else left = mid+1;
    }
    return answer;
}