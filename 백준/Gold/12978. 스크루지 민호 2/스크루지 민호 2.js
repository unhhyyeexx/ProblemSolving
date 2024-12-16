const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [u, v] = input[i].trim().split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

function solution() {
  const visit = Array(n + 1).fill(0);
  const dp = Array.from({ length: n + 1 }, () => [0, 1]);

  function dfs(now) {
    for (const next of graph[now]) {
      if (visit[next] === 0) {
        visit[next] = 1;
        dfs(next);

        dp[now][1] += Math.min(dp[next][0], dp[next][1]);
        dp[now][0] += dp[next][1];
      }
    }
    return;
  }

  visit[1] = 1;
  dfs(1);
  console.log(Math.min(dp[1][0], dp[1][1]));
}

solution();