const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

function factorial(n) {
    if (n === 0 || n === 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function countAnagrams(freqMap) {
    let total = Object.values(freqMap).reduce((sum, val) => sum + val, 0);
    let denominator = Object.values(freqMap).reduce((prod, val) => prod * factorial(val), 1);
    return factorial(total) / denominator;
}

function findKthAnagram(word, k) {
    let freqMap = {};
    for (let char of word) {
        freqMap[char] = (freqMap[char] || 0) + 1;
    }

    let result = "";
    let remainingK = k - 1; // K는 1-based index이므로 0-based로 변환

    while (Object.values(freqMap).reduce((a, b) => a + b, 0) > 0) {  // 모든 문자가 사라질 때까지 반복
        let sortedKeys = Object.keys(freqMap).sort(); // 사전순 정렬

        for (let char of sortedKeys) {
            if (freqMap[char] === 0) continue;

            // 현재 문자를 첫 글자로 배치했을 때 만들 수 있는 애너그램 개수
            freqMap[char]--;
            let numAnagrams = countAnagrams(freqMap);

            if (remainingK < numAnagrams) {
                result += char;
                if (freqMap[char] === 0) delete freqMap[char]; // 빈도수가 0이면 삭제
                break;
            } else {
                remainingK -= numAnagrams;
                freqMap[char]++; // 원상 복구
            }
        }
    }

    return result;
}

let index = 0;
while (true){
    const [word, k] = input[index++].split(" ");
    if (word === "#") break;
    console.log(findKthAnagram(word, k));
}