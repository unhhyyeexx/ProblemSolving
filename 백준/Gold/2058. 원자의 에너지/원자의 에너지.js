const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 원자의 에너지 상태 == 노드
// 어떤 노드값에서 어떤 양성자를 더하거나 빼서 다른 노드 값이 나온다면 두 노드는 서로 연결돼있음
// 자식노드가 지신을 포함한 최댓값과 자신을 포함하지 않은 최댓값을 배열로 보내주면,
// 현재 노드도 자신을 포함한 최댓값과 자신을 포함하지 않은 최댓값을 배열로 리턴

const [n, m] = input[0].split(" ").map(Number);
const atom = [];
const proton = [];
for (let i = 1; i < n + 1; i++) {
  atom.push(+input[i].trim());
}

for (let i = n + 1; i < m + n + 1; i++) {
  proton.push(+input[i].trim());
}

function solution() {
  const visit = Array.from({ length: 1000001 }, () => 0);

  function dfs(now) {
    visit[now] = 1; // 순환 방지

    // now를 포함할 때 최댓갑, now를 포함안할때 최댓값
    const maxValue = [now, 0];

    let tmp = 0;
    for (let i = 0; i < m; i++) {
      // 양성자 받아들이기
      let newAtom = now + proton[i];
      if (
        newAtom > 0 &&
        newAtom < 1000000000 &&
        atom.includes(newAtom) &&
        !visit[newAtom]
      ) {
        tmp = dfs(newAtom);
        maxValue[0] += tmp[1];
        maxValue[1] += Math.max(tmp[0], tmp[1]);
      }
        // 양성자 내쏘기
      newAtom = now - proton[i];
      if (
        newAtom > 0 &&
        newAtom < 1000000000 &&
        atom.includes(newAtom) &&
        !visit[newAtom]
      ) {
        tmp = dfs(newAtom);
        maxValue[0] += tmp[1];
        maxValue[1] += Math.max(tmp[0], tmp[1]);
      }
    }
    return maxValue;
  }

  let answer = dfs(atom[0]);
  console.log(Math.max(...answer));
}

solution();