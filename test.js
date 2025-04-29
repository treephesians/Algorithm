const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let index = 0;
const [N, K] = input[index++].split(" ").map(Number);
const dp = Array.from({ length: N + 1 }, () => Array(K + 1).fill(0));

for (let i = 1; i <= N; i++) {
  const [W, V] = input[index++].split(" ").map(Number);
  for (let w = 0; w <= K; w++) {
    dp[i][w] = dp[i - 1][w];              // 일단 안 담는다
    if (w >= W) {
      dp[i][w] = Math.max(
        dp[i][w],
        dp[i - 1][w - W] + V              // 담았을 때
      );
    }
  }
}

console.log(dp[N][K]);
