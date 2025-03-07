const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

// 8 10
// 1 2 2
// 2 6 3
// 2 7 2
// 1 3 1
// 3 7 2
// 4 7 5
// 5 6 2
// 5 7 2
// 7 8 2
// 5 8 2
// 3 6

let index = 0;
const [V, M] = input[index++].split(" ").map(Number);
const matrix = Array.from({length: V}, ()=>Array(V).fill(Infinity));

for (let i = 0; i < V; i++){
    matrix[i][i] = 0;
}

for (let i = 0; i < M; i++){
    const [nodeA, nodeB, cost] = input[index++].split(" ").map(Number);
    matrix[nodeA - 1][nodeB - 1] = Math.min(matrix[nodeA - 1][nodeB - 1], cost);
    matrix[nodeB - 1][nodeA - 1] = Math.min(matrix[nodeB - 1][nodeA - 1] , cost);
}

const [start, end] = input[index++].split(" ").map(Number);

for (let k = 0; k < V; k++){
    for (let i = 0; i < V; i++){
        for (let j = 0; j < V; j++){
            matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
        }
    }
}

let result = [];
let min_distance = Infinity;
for (let i = 0; i < V; i++){
    if (i + 1 !== start && i + 1 !== end){
        if (matrix[start - 1][i] + matrix[i][end - 1] < min_distance){
            result = [];
            min_distance = matrix[start - 1][i] + matrix[i][end - 1];
        }
        if (matrix[start - 1][i] + matrix[i][end - 1] == min_distance && matrix[start - 1][i] <= matrix[i][end - 1]){
            result.push([matrix[start - 1][i], i]);
        }
    }
}

result.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    return a[1] - b[1];
});

if (result.length == 0) console.log(-1);
else console.log(result[0][1] + 1);