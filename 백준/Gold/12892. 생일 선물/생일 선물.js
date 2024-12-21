const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, d] = input[0].trim().split(" ").map(Number);
const graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  graph.sort((a, b) => a[0] - b[0]);
  let left = 0,
    right = 0;
  let answer = 0;
  let sumV = 0;
  while (right < n) {
    if (graph[right][0] - graph[left][0] < d) {
      sumV += graph[right][1];
      answer = Math.max(sumV, answer);
      right += 1;
    } else {
      sumV -= graph[left][1];
      left += 1;
    }
  }
  console.log(answer);
}

solution();