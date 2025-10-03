/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    for (let i = prices.length - 1; i > 0; i--) {
        prices[i] = prices[i] - prices[i - 1];
    }
    prices[0] = 0;
    const answer = prices.reduce((count, val, _index) => {
        if (val > 0) count += val;
        return count;
    }, 0);

    return answer;
};

// Input: prices = [7,1,5,3,6,4]
// Output: 7

prices = [7,1,5,3,-1,6]
prices2 = [0,-6,4,-2,-4,7]
console.log(maxProfit(prices));
