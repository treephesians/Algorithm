const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let T = 1; // TestCase 여러 개이면 여기를 수정해야한다.
const inputs = [];
let count = 0;

rl.on("line", (line) => {
  if (T === undefined) {
    T = parseInt(line.trim(), 10);
  } else {
    inputs.push(line.trim());
    count++;

    if (count === T) {
      rl.close();
    }
  }
});

rl.on("close", () => {});
