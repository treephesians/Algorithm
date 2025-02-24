const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let idx = 0;
const N = parseInt(input[idx++]); // 방의 개수
const C = input[idx++].split(" ").map(Number); // 각 방에 연결된 쪽방의 개수

// 만약 방이 하나라면, 그 방에만 배치 가능 (쪽방이 있다면 배치할 수 없으므로)
if (N === 1) {
    console.log(C[0] === 0 ? 1 : C[0]);
    process.exit();
}

// 각 방에 대해 두 가지 옵션의 값을 정리
// Option A: 방을 사용 → yield = 1
// Option B: 방을 사용하지 않음 → yield = C[i]
const A = Array(N).fill(1);      // 방을 사용하는 경우 (항상 1)
const B = C.slice();             // 방을 사용하지 않고 쪽방만 사용하는 경우

// 함수: 선형 체인에 대한 DP 계산 (방 0부터 N-1까지)
// 시작 상태에 따라 dp[0][0] 또는 dp[0][1]을 강제합니다.
function linearDP(startUsed) {
    // dp[i][0]: i번째 방을 사용하지 않은 경우
    // dp[i][1]: i번째 방을 사용한 경우
    const dp = Array.from({ length: N }, () => [0, 0]);

    if (startUsed) {
        // 케이스 1: 방 0을 사용
        dp[0][1] = A[0];    // 1
        dp[0][0] = -Infinity; // 방 0을 사용하지 않으면 안됨 (강제)
    } else {
        // 케이스 2: 방 0을 사용하지 않음
        dp[0][0] = B[0];    // C[0]
        dp[0][1] = -Infinity; // 강제로 사용하면 안 됨
    }

    for (let i = 1; i < N; i++) {
        // i번째 방을 사용하지 않는 경우: 그 이전 방은 상관 없이 선택 가능
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]) + B[i];
        // i번째 방을 사용하는 경우: 이전 방은 반드시 사용하지 않아야 함
        dp[i][1] = dp[i - 1][0] + A[i];
    }

    return dp;
}

// 케이스 1: 방 0을 사용 → 최종적으로 방 N-1는 사용하지 않아야 함
const dpCase1 = linearDP(true);
const case1 = dpCase1[N - 1][0];  // 방 N-1 사용 금지

// 케이스 2: 방 0을 사용하지 않음
const dpCase2 = linearDP(false);
const case2 = Math.max(dpCase2[N - 1][0], dpCase2[N - 1][1]);

const answer = Math.max(case1, case2);
console.log(answer);