const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const { exit } = require("process");

const words = input[0].trim().split(" ");

// 문자 리스트 생성
const uniqueChars = [...new Set(words[0] + words[1] + words[2])];
if (uniqueChars.length > 10) {
  console.log("NO");
  exit();
}

const charToDigit = Array(128).fill(-1);
const usedDigits = Array(10).fill(false);

function wordToNumber(word) {
  let num = 0;
  for (let char of word) {
    num = num * 10 + charToDigit[char.charCodeAt(0)];
  }
  return num;
}

function backtrack(index) {
  if (index === uniqueChars.length) {
    const num1 = wordToNumber(words[0]);
    const num2 = wordToNumber(words[1]);
    const num3 = wordToNumber(words[2]);

    // 숫자가 합 조건을 만족하면 YES 출력
    if (num1 + num2 === num3) {
      console.log("YES");
      process.exit();
    }
    return;
  }

  for (let digit = 0; digit < 10; digit++) {
    if (!usedDigits[digit]) {
      charToDigit[uniqueChars[index].charCodeAt(0)] = digit;
      usedDigits[digit] = true;

      // 다음문자 탐색
      backtrack(index + 1);

      // 백트래킹 복구
      charToDigit[uniqueChars[index].charCodeAt(0)] = -1;
      usedDigits[digit] = false;
    }
  }
}

backtrack(0);
console.log("NO");
