/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let min_num = Infinity;
    let max_profit = 0;
    for (let i = 0; i < prices.length; i++) {
        min_num = Math.min(min_num, prices[i]);
        max_profit = Math.max(max_profit, prices[i] - min_num);
    }
    return max_profit;
};
