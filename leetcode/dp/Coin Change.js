/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = Array(amount + 1).fill(Infinity);

    if (amount === 0) return 0;

    for (let coin of coins) dp[coin] = 1;

    for (let i = 1; i < amount + 1; i++) {
        for (let coin of coins) {
            if (i + coin < amount + 1) {
                dp[i + coin] = Math.min(dp[i + coin], dp[i] + 1);
            }
        }
    }

    return dp[amount] !== Infinity ? dp[amount] : -1;
};