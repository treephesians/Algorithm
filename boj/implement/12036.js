const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let index = 0;
const T = parseInt(input[index++]);

for (let i = 0; i < T; i++) {
    let [D, K, N] = input[index++].split(" ").map(Number);
    
    // N을 최적화된 값으로 줄이기 (주기성을 활용)
    N %= (D / 2);

    let finalPos;
    if (K % 2 === 1) {
        // 홀수 번째 시작: +2씩 증가
        finalPos = (K + 2 * N) % D;
        if (finalPos === 0) finalPos = D;
    } else {
        // 짝수 번째 시작: -2씩 감소
        finalPos = (K - 2 * N);
        if (finalPos <= 0) finalPos += D;
    }

    // 좌우 이웃 찾기
    let left = (finalPos === D) ? 1 : finalPos + 1;
    let right = (finalPos === 1) ? D : finalPos - 1;

    console.log(`Case #${i + 1}: ${left} ${right}`);
}