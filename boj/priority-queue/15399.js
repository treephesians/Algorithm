const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let index = 0;
const n = parseInt(input[index++]);
const arr = [];

let v = 0;
let distance = 0;
for (let i = 0; i < n; i++){
    const [a, t] = input[index++].split(" ").map(Number);
    distance += v * t + a * t * t / 2;
    v += a * t;
    arr.push([a, t]);
}

arr.sort((a, b) => b[0] * b[1] - a[0] * a[1]);

let max_v = 0;
let max_distance = 0;
for (let i = 0; i < n; i++){
    const [a, t] = arr[i];
    max_distance += max_v * t + a * t * t / 2;
    max_v += a * t;
}

console.log((max_distance - distance).toFixed(1));