const fs = require("fs");
//const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const input = fs.readFileSync("boj/input.txt").toString().trim().split("\n");

const [N, r, c] = input[0].split(" ").map(Number)

function Z (N, r, c) {
    if (N == 0) return 0;
    const half_size = Math.pow(2, N - 1);
    const numbers = half_size * half_size;
    if (r < half_size && c < half_size) 
        return Z(N - 1, r, c);
    if (r < half_size && c >= half_size)
        return numbers + Z(N - 1, r, c - half_size);
    if (r >= half_size && c < half_size)
        return 2 * numbers + Z(N - 1, r - half_size, c);
    if (r >= half_size && c >= half_size)
        return 3 * numbers + Z(N - 1, r - half_size, c - half_size);
}

console.log(Z(N, r, c))