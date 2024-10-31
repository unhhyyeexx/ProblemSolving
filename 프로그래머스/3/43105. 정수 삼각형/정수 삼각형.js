function solution(triangle) {
    var answer = 0;
    const n = triangle.length;
    
    // i는 행, j는 열
    for (let i=1; i<n; i++) {
        for (let j=0; j<i+1; j++){
            if (j === 0) {
                // 1열에서는 한칸 위에만 본다.
                triangle[i][j] += triangle[i-1][j];
            } else if (j === i) {
                // 막열에서는 한칸 위, 한칸 왼쪽을 본다.
                triangle[i][j] += triangle[i-1][j-1];
            } else{
                // 중간열은 위랑, 위왼쪽 둘이 비교
                triangle[i][j] += Math.max(triangle[i-1][j], triangle[i-1][j-1]);
            }
        }
    }
    answer = Math.max(...triangle[n-1])
    return answer;
}