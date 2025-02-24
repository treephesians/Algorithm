const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

// 5 5
// 1 0 1 0 1
// 0 0 1 1 1
// 1 0 1 0 0
// 0 1 1 0 1
// 1 0 1 0 1

let index = 0;
const [N, M] = input[index++].split(" ").map(Number);
const matrix = Array(N);

for (let i = 0; i < N; i++) matrix[i] = input[index++].split(" ").map(Number);

let count = 0;

for (let row = 1; row < N; row++){
    for (let col = 0; col < M; col++){
        if (matrix[row][col]){
            matrix[row][col] = matrix[row - 1][col];
            if (0 < col) matrix[row][col] += matrix[row - 1][col - 1];
            if (col < M - 1) matrix[row][col] += matrix[row - 1][col + 1];
            matrix[row][col] %= 1000000007;
        }
    }
}

let result = 0;
for (let col = 0; col < M; col++){
    result += matrix[N - 1][col];
    result %= 1000000007;
}

console.log(result);