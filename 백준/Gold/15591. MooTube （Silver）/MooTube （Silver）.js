const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, Q] = input[0].trim().split(" ").map(Number);
const graph = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [a, b, c] = input[i].trim().split(" ").map(Number);
  graph[a].push([b, c]);
  graph[b].push([a, c]);
}

for (let i = n; i < n + Q; i++) {
  const [k, v] = input[i].trim().split(" ").map(Number);
  const visit = Array(n + 1).fill(false);
  visit[v] = true;
  let result = 0;
  const q = [[v, Infinity]];

  while (q.length > 0) {
    const [v, usado] = q.shift();
    for (let [next_v, next_u] of graph[v]) {
      next_u = Math.min(usado, next_u);
      if (next_u >= k && !visit[next_v]) {
        result += 1;
        q.push([next_v, next_u]);
        visit[next_v] = true;
      }
    }
  }
  console.log(result);
}
