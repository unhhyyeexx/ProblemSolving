const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let T = parseInt(input[0]);
let index = 1;

for (let tc = 0; tc < T; tc++) {
  let sudoku = [];
  let rCheck = Array.from({ length: 9 }, () => Array(10).fill(false));
  let cCheck = Array.from({ length: 9 }, () => Array(10).fill(false));
  let sCheck = Array.from({ length: 9 }, () => Array(10).fill(false));
  let stack = [];
  let isValid = true;

  for (let i = 0; i < 9; i++) {
    let row = input[index++].trim().split("").map(Number);
    sudoku.push(row);

    for (let j = 0; j < 9; j++) {
      let val = row[j];
      if (val !== 0) {
        if (
          rCheck[i][val] ||
          cCheck[j][val] ||
          sCheck[Math.floor(i / 3) * 3 + Math.floor(j / 3)][val]
        ) {
          isValid = false;
        }
        rCheck[i][val] = true;
        cCheck[j][val] = true;
        sCheck[Math.floor(i / 3) * 3 + Math.floor(j / 3)][val] = true;
      } else {
        stack.push([i, j]);
      }
    }
  }

  function backtracking(level) {
    if (level === stack.length) {
      return true;
    }

    let [r, c] = stack[level];
    for (let j = 1; j <= 9; j++) {
      if (
        !rCheck[r][j] &&
        !cCheck[c][j] &&
        !sCheck[Math.floor(r / 3) * 3 + Math.floor(c / 3)][j]
      ) {
        sudoku[r][c] = j;
        rCheck[r][j] = true;
        cCheck[c][j] = true;
        sCheck[Math.floor(r / 3) * 3 + Math.floor(c / 3)][j] = true;

        if (backtracking(level + 1)) {
          return true;
        }

        sudoku[r][c] = 0;
        rCheck[r][j] = false;
        cCheck[c][j] = false;
        sCheck[Math.floor(r / 3) * 3 + Math.floor(c / 3)][j] = false;
      }
    }
    return false;
  }
  
  if (isValid && backtracking(0)) {
    if (tc !== 0) {
      console.log(" ");
    }
    for (let i = 0; i < 9; i++) {
      console.log(sudoku[i].join(""));
    }
  } else {
    if (tc !== 0) {
      console.log(" ");
    }
    console.log("Could not complete this grid.");
  }
}