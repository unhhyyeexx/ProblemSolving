const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input[0].trim().split(" ").map(Number);
let graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].trim().split(" ").map(Number));
}

function solution() {
  graph.sort((a, b) => a[1] - b[1] || b[0] - a[0]);

  let weight = 0;
  let same = 0;
  let flag = 0;

  let answer = Infinity;

  for (let i = 0; i < n; i++) {
    weight += graph[i][0];
    if (i >= 1 && graph[i][1] === graph[i - 1][1]) {
      same += graph[i][1];
    } else {
      same = 0;
    }

    if (weight >= m) {
      answer = Math.min(answer, graph[i][1] + same);
      flag = 1;
    }
  }

  console.log(flag === 1 ? answer : -1);
}

solution();