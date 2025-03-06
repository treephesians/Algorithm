const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

// 5 10
// 3
// 4
// 6
// 100
// 1

// 6 11
// 3
// 4
// 5
// 100
// 1

let index = 0;
const [N, M] = input[index++].split(" ").map(Number);
const dp = Array(N + 1).fill(0);

let sum = M;
for (let i = 1; i <= N; i++){
    dp[i] = parseInt(input[index++]) + sum;
    sum = dp[i];
}

for (let i = 2; i <= N; i++){
    for (let j = 1; j < i; j++){
        dp[i] = Math.min(dp[i], dp[j] + dp[i - j] + M);
    }
}

console.log(dp[N]);

