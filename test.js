/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // set, start, end = 0에서 시작
    // end 를 늘리다가 중복이 나타나면 while로 그 중복을 없앨때까지 줄여야 함.
    // max_size 사용
    // 이 때 "" 빈 문자열 잘 고려해야 함

    const set = new Set();
    let max_size = 0, start = 0;
    let max_idx = [0, 0];
    for (let end = 0; end < s.length; end++) {
        if (set.has(s[end])) {
            while (s[start] !== s[end]) {
                set.delete(s[start]);
                start++;
            }
            start++
            continue;
        }
        set.add(s[end]);
        if (end - start + 1 > max_size) {
            max_size = end - start + 1;
        }
    }
    return max_size;
};

// "zabcadfbcbb"