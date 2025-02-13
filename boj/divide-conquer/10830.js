const fs = require("fs");
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

let [N, B] = input[0].split(" ").map(Number);

let matrix = Array(N);

for (let i = 1; i <= N; i++){
    matrix[i - 1] = input[i].split(" ").map(Number);
}

function matrix_multiply(matrix1, matrix2){
    const size = matrix1.length;
    const new_matrix = Array.from({length : size}, ()=>Array(size).fill(0));

    for (let row = 0; row < size; row++){
        for (let col = 0; col < size; col++){
            result = 0;
            for (let i = 0; i < size; i ++){
                result += matrix1[row][i] * matrix2[i][col];
            }
            new_matrix[row][col] = result % 1000;
        }
    }

    return new_matrix;
}

let base = Array.from({length: N}, () => Array(N).fill(0));
for (let i = 0; i < N; i++){
    base[i][i] = 1
}

while (B > 0) {

    if (B % 2 != 0){
        base = matrix_multiply(base, matrix);
        B -= 1;
    }
    else {
        matrix = matrix_multiply(matrix, matrix);
        B /= 2;
    }
}

for (let i = 0; i < N; i++){
    console.log(base[i].join(" "));
}