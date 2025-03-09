function solution(n, money) {
    const dp = Array(n + 1).fill(0); 
    dp[0] = 1; // n이 0일 때는 한 가지 경우 (아무 동전도 사용하지 않는 경우)

    for (const coin of money) {
        for (let i = coin; i <= n; i++) {
            dp[i] += dp[i - coin]; // i원을 만들 수 있는 경우의 수 갱신
            dp[i] %= 1000000007; // 모듈러 연산
        }
    }

    return dp[n];
}

const n = 5;
const money = [1, 2, 5];
console.log(solution(n, money)); // 출력: 4