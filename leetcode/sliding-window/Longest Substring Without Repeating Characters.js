/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0, max_length = 0;
    const set = new Set();

    for (let end = 0; end < s.length; end++) {
        while (set.has(s[end])) {
            set.delete(s[start++]);
        }
        console.log(start, end)
        set.add(s[end]);
        max_length = Math.max(max_length, end - start + 1)
    }
    return max_length
};