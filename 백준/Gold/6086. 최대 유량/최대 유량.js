const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = +input[0];
const graph = [];
for (let i = 1; i < n + 1; i++) {
  graph.push(input[i].trim().split(" "));
}

function bfs(s, process, flow) {
  const q = [];
  q.push(s);

  visit = Array(128).fill(-1);
  visit[s] = s;

  while (q.length > 0) {
    const idx = q.shift();
    for (let i = 65; i < 123; i++) {
      if (visit[i] === -1 && process[idx][i] - flow[idx][i] > 0) {
        q.push(i);
        visit[i] = idx;
      }
    }
  }

  return visit;
}

function merge(process) {
  let s = 65,
    e = 90;
  const flow = Array.from({ length: 128 }, () => Array(128).fill(0));
  let res = 0;

  while (true) {
    const parent = bfs(s, process, flow);
    if (parent[e] === -1) {
      return res;
    }

    let minV = 2147483647;

    let idx = e;
    while (idx !== s) {
      minV = Math.min(minV, process[parent[idx]][idx] - flow[parent[idx]][idx]);
      idx = parent[idx];
    }

    idx = e;
    while (idx !== s) {
      flow[parent[idx]][idx] += minV;
      flow[idx][parent[idx]] -= minV;
      idx = parent[idx];
    }

    res += minV;
  }
}

function solution() {
  const process = Array.from({ length: 128 }, () => Array(128).fill(0));
  for (let i = 0; i < n; i++) {
    let [u, v, x] = graph[i];
    u = u.charCodeAt();
    v = v.charCodeAt();
    x = +x;
    process[u][v] += x;
    process[v][u] += x;
  }

  console.log(merge(process));
}

solution();