const fs = require("fs")
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

const N = parseInt(input[0])

const matrix = Array.from({length:N}, ()=>Array(N).fill("*"))

function O(N, row, col){
    if (N == 1) return;
    const size = N / 3;
    for (let i = row + size; i < row + 2 * size; i++){
        for (let j = col + size; j < col + 2 * size; j++){
            matrix[i][j] = " ";
        }
    }
    O(N / 3, row, col);
    O(N / 3, row + size, col);
    O(N / 3, row + 2 * size, col);
    O(N / 3, row, col + size);
    O(N / 3, row, col + 2 * size);
    O(N / 3, row + size, col + 2 * size);
    O(N / 3, row + 2 * size, col + size);
    O(N / 3, row + 2 * size, col + 2 * size);
}

O(N, 0, 0);

for (let row = 0; row < N; row++){
    console.log(matrix[row].join(""));
}