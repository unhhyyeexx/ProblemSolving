const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, k] = input[0].split(" ").map(Number);
const costs = input.slice(1).map(line => line.split(" ").map(Number));


function solution(n, k, costs) {
  let maxDistance = -1;
  let endNode = 0;

  const graph = Array.from({ length: n }, () => []);
  const edges = [...costs];

  edges.sort((a, b) => a[2] - b[2]);

  const roots = Array.from({ length: n }, (_, i) => i);

  function find(x) {
    if (roots[x] !== x) {
      roots[x] = find(roots[x]);
    }
    return roots[x];
  }

  function union(x, y) {
    x = find(x);
    y = find(y);
    if (x === y) return false;
    if (x < y) roots[y] = x;
    else roots[x] = y;
    return true;
  }

  let minCost = 0;
  for (const [a, b, cost] of edges) {
    if (union(a, b)) {
      graph[a].push([b, cost]);
      graph[b].push([a, cost]);
      minCost += cost;
    }
  }

  function dfs(v, total, visit) {
    if (total > maxDistance) {
      maxDistance = total;
      endNode = v;
    }

    for (const [next, cost] of graph[v]) {
      if (visit[next]) continue;
      visit[next] = true;
      dfs(next, total + cost, visit);
    }
  }

  let visit = Array(n).fill(false);
  visit[0] = true;
  dfs(0, 0, visit);

  visit = Array(n).fill(false);
  visit[endNode] = true;
  dfs(endNode, 0, visit);

  console.log(minCost);
  console.log(maxDistance);
}

solution(n, k, costs);