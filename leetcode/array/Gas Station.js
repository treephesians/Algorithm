/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    const n = gas.length;
    for (let i = 0; i < n; i++) {
        if (gas[i] < cost[i]) continue;
        let g = gas[i] - cost[i];
        for (let j = 1; j < n; j++) {
            const idx = (i + j) % n;
            g += gas[idx] - cost[idx];
            console.log(idx, g);

            if (g <= 0) break;
        }
        if (g <= 0) continue;
        return i;
    }
    return -1;
};

console.log(canCompleteCircuit([4,5,2,6,5,3], [3,2,7,3,2,9]));