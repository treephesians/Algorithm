const fs = require("fs");
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);

const dp = Array.from({length : N + 1}, () => Array(K).fill(1));

for (let row = 1; row < N + 1; row++){
    for (let col = 1; col < K; col++){
        dp[row][col] = (dp[row - 1][col] + dp[row][col - 1]) % 1000000000;
    }
}

console.log(dp[N][K - 1]);