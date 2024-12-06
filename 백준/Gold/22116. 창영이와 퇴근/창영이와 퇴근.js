const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

class Heap {
  constructor() {
    this.heap = [];
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  push(value) {
    this.heap.push(value);
    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor((currentIdx - 1) / 2);

    while (
      this.heap[parentIdx] &&
      this.heap[parentIdx][0] > this.heap[currentIdx][0]
    ) {
      this.swap(currentIdx, parentIdx);
      currentIdx = parentIdx;
      parentIdx = Math.floor((currentIdx - 1) / 2);
    }
  }

  pop() {
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const returnValue = this.heap[0];
    this.heap[0] = this.heap.pop();

    let currentIdx = 0;
    let leftIdx = currentIdx * 2 + 1;
    let rightIdx = currentIdx * 2 + 2;

    while (
      (this.heap[leftIdx] &&
        this.heap[leftIdx][0] < this.heap[currentIdx][0]) ||
      (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[currentIdx][0])
    ) {
      let smallerIdx = leftIdx;
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx][0] < this.heap[smallerIdx][0]
      ) {
        smallerIdx = rightIdx;
      }

      this.swap(currentIdx, smallerIdx);
      currentIdx = smallerIdx;
      leftIdx = currentIdx * 2 + 1;
      rightIdx = currentIdx * 2 + 2;
    }
    return returnValue;
  }
}

const n = +input[0];
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].trim().split(" ").map(Number));
}
const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const maxSize = 10000000000;
visit = Array.from({ length: n }, () => Array(n).fill(maxSize));

function dijkstra(a, b) {
  let q = new Heap();
  q.push([0, a, b]);
  visit[a][b] = 0;

  while (!q.isEmpty()) {
    const [h, i, j] = q.pop();
    if (i === n - 1 && j === n - 1) {
      console.log(h);
      break;
    }

    if (visit[i][j] < h) continue;

    for ([di, dj] of dir) {
      const ni = i + di;
      const nj = j + dj;
      if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;

      const diff = Math.abs(board[ni][nj] - board[i][j]);
      const nh = Math.max(h, diff);

      if (visit[ni][nj] > nh) {
        visit[ni][nj] = nh;
        q.push([nh, ni, nj]);
      }
    }
  }
}

dijkstra(0, 0);
