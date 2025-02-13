const fs = require("fs")
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

const N = parseInt(input[0])

const matrix = Array.from({length:N}, ()=>Array(N).fill("*"))

console.log(matrix)