const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, x] = input[0].trim().split(" ").map(Number);

function dnc(n, x) {
  // 현재 먹어야 하는 장 수가 1장이면 패티는 0장
  if (x === 1) return 0;

  // 현재 먹어야 하는 장 수가 번과 n-1버거 미만이면
  // 맨 앞 번을 빼고 분할 정복
  if (x < dp1[n - 1] + 1) {
    return dnc(n - 1, x - 1);
  }

  // 현재 먹어야 하는 장 수가 번과 n-1버거이면
  // n-1 버거의 패티 수
  if (x === dp1[n - 1] + 1) {
    return dp2[n - 1];
  }

  // 현재 먹어야 하는 장 수가 번과 n-1버거와 패티이면
  // n-1 버거의 패티수 + 1
  if (x === dp1[n - 1] + 2) {
    return dp2[n - 1] + 1;
  }

  // 현재 먹어야 하는 장 수가 번과 첫번째 n-1버거+ 패티 + n-1버거 내부부
  // 첫 n-1버거의 패티 수 + 중간 패티 한 장 + 나머지 뒷 부분 분할 정복 결과
  if (x < dp1[n - 1] * 2 + 2) {
    return dp2[n - 1] + 1 + dnc(n - 1, x - dp1[n - 1] - 2);
  }

  // 현재 먹어야 하는 장 수가 n버거 레이어 수와 동일하거나 1 작다면
  // n버거의 패티 수
  return dp2[n];
}

const dp1 = Array(n + 1).fill(0); // 레이어의 수
const dp2 = Array(n + 1).fill(0); // 패티의 개수
// 레벨 0의 버거는 패티만으로 이루어져있음
dp1[0] = 1;
dp2[0] = 1;

for (let i = 1; i < n + 1; i++) {
  // 레벨-L버거는 <번, 레벨-L-1버거, 패티, 레벨-L-1버거, 번>
  dp1[i] = dp1[i - 1] * 2 + 3;
  dp2[i] = dp2[i - 1] * 2 + 1;
}

console.log(dnc(n, x));