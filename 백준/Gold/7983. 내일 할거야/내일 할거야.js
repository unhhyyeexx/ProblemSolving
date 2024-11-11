const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = Number(input[0]);
const tasks = [];
for (let i = 1; i < input.length; i++) {
  tasks.push(
    input[i]
      .toString()
      .trim()
      .split(" ")
      .map((e) => Number(e))
  );
}

function solution(n, tasks) {
  tasks.sort((a, b) => b[1] - a[1]);
  let answer = tasks[0][1];

  for (let i = 0; i < n; i++) {
    answer = Math.min(tasks[i][1], answer) - tasks[i][0];
  }

  console.log(answer);
}

solution(n, tasks);