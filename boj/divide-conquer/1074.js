const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const input = fs.readFileSync("../input.txt").toString().trim().split(" ");

const [N, r, c] = input.map(Number);

function zTraversal(n, x, y) {
    if (n === 0) return 0; // 가장 작은 크기가 되면 0 반환

    let half = 1 << (n - 1); // 2^(n-1) 크기
    let quadrantSize = half * half; // 한 사분면의 크기

    if (x < half && y < half) {
        // 1️⃣ 왼쪽 위 (0번째)
        return zTraversal(n - 1, x, y);
    } else if (x < half && y >= half) {
        // 2️⃣ 오른쪽 위 (1번째)
        return quadrantSize + zTraversal(n - 1, x, y - half);
    } else if (x >= half && y < half) {
        // 3️⃣ 왼쪽 아래 (2번째)
        return 2 * quadrantSize + zTraversal(n - 1, x - half, y);
    } else {
        // 4️⃣ 오른쪽 아래 (3번째)
        return 3 * quadrantSize + zTraversal(n - 1, x - half, y - half);
    }
}

// 결과 출력
console.log(zTraversal(N, r, c));