const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let idx = 0;
while (input[idx] !== "0") {
  const n = +input[idx];
  const visit = Array(n).fill(0);
  let answer = 0;
  const graph = [];
  for (let i = idx + 1; i < idx + n + 1; i++) {
    const tmp = input[i].trim().split(" ");
    graph.push([tmp[0], +tmp[1], tmp.slice(2, -1)]);
  }

  function dfs(room, money) {
    if (answer === 1) return;

    const [kind, cost, arr] = graph[room];
    if (kind === "L") {
      // 레프리콘
      if (cost > money) {
        money = cost;
      }
    } else if (kind === "T") {
      // 트롤
      if (cost > money) return;
      else {
        money -= cost;
      }
    }

    if (room === n - 1) {
      answer = 1;
      return;
    }

    visit[room] = 1;
    for (const nroom of arr) {
      if (visit[+nroom - 1] === 0) {
        dfs(+nroom - 1, money);
      }
    }
    visit[room] = 0;
  }

  dfs(0, 0);

  if (answer === 0) {
    console.log("No");
  } else {
    console.log("Yes");
  }

  idx += n + 1;
}