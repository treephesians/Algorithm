function perfectShuffle(n, shuffleType) {
    let originalDeck = Array.from({ length: n }, (_, i) => i); // 원래 덱 [0, 1, ..., n-1]
    let currentDeck = [...originalDeck]; // 현재 덱
    let count = 0;

    while (true) {
        count++;

        // 덱을 두 개의 절반으로 나누기
        let half1, half2;
        if (n % 2 === 0) {
            half1 = currentDeck.slice(0, n / 2);
            half2 = currentDeck.slice(n / 2);
        } else {
            if (shuffleType === "out") {
                half1 = currentDeck.slice(0, Math.ceil(n / 2));
                half2 = currentDeck.slice(Math.ceil(n / 2));
            } else { // in-shuffle
                half1 = currentDeck.slice(0, Math.floor(n / 2));
                half2 = currentDeck.slice(Math.floor(n / 2));
            }
        }

        // 새로운 덱 생성
        let shuffledDeck = [];
        if (shuffleType === "out") {
            for (let i = 0; i < half2.length; i++) {
                shuffledDeck.push(half1[i]);
                shuffledDeck.push(half2[i]);
            }
            if (half1.length > half2.length) {
                shuffledDeck.push(half1[half1.length - 1]);
            }
        } else { // in-shuffle
            for (let i = 0; i < half1.length; i++) {
                shuffledDeck.push(half2[i]);
                shuffledDeck.push(half1[i]);
            }
            if (half2.length > half1.length) {
                shuffledDeck.push(half2[half2.length - 1]);
            }
        }

        // 현재 덱을 갱신
        currentDeck = shuffledDeck;

        // 원래 상태로 돌아왔는지 확인
        if (JSON.stringify(currentDeck) === JSON.stringify(originalDeck)) {
            break;
        }
    }

    return count;
}

// 입력 받기
const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");
const [n, shuffleType] = input[0].split(" ");
const result = perfectShuffle(parseInt(n, 10), shuffleType);

// 결과 출력
console.log(result);