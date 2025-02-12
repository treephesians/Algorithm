const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
//const input = fs.readFileSync("../input.txt").toString().trim().split("\n");

const n = parseInt(input[0]); // 도시의 개수