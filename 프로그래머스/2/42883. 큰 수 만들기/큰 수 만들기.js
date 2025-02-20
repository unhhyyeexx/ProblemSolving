function solution(number, k) {
  number = number.split("").map(Number);
  const n = number.length - k;
  let answer = number.slice(k);
  for (let i = k - 1; i >= 0; i--) {
    let now = number[i];
    let j = 0;
    while (now >= answer[j] && j < n) {
      const tmp = now;
      now = answer[j];
      answer[j] = tmp;
      j += 1;
    }
  }
    return answer.join("");
}