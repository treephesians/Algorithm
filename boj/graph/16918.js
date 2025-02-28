const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");

let idx = 0;
const [R, C, T] = input[idx++].split(" ").map(Number);
const initial = [];
for (let i = 0; i < R; i++){
    initial.push(input[idx++].split(""));
}

// 전체 폭탄 판: 모든 칸에 'O' 채우기
function fullBoard() {
    const board = [];
    for (let i = 0; i < R; i++){
        board.push(new Array(C).fill("O"));
    }
    return board;
}

// 폭발 시뮬레이션 함수
// 주어진 board에서 폭탄('O')가 있는 칸과 그 인접한 네 칸을 빈칸('.')으로 바꾼 새 보드를 반환
function explode(board) {
    const res = fullBoard();  // 시작은 전체 폭탄 판
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    for (let r = 0; r < R; r++){
        for (let c = 0; c < C; c++){
            if (board[r][c] === "O") {
                res[r][c] = ".";
                for (let k = 0; k < 4; k++){
                    const nr = r + dr[k];
                    const nc = c + dc[k];
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                        res[nr][nc] = ".";
                    }
                }
            }
        }
    }
    return res;
}

// 시간에 따른 보드 상태 결정
if (T === 1) {
    // 1초일 때: 초기 상태 그대로 출력
    console.log(initial.map(row => row.join("")).join("\n"));
} else if (T % 2 === 0) {
    // 짝수 초일 때: 전체가 폭탄 판
    const board = fullBoard();
    console.log(board.map(row => row.join("")).join("\n"));
} else {
    // T가 홀수이고 T > 1인 경우:
    // state1: 초기 상태의 폭탄들이 폭발한 결과 (3초 상태)
    const state1 = explode(initial);
    // state2: state1의 폭탄들이 폭발한 결과 (5초 상태)
    const state2 = explode(state1);
    if (T % 4 === 3) {
        console.log(state1.map(row => row.join("")).join("\n"));
    } else { // T % 4 === 1
        console.log(state2.map(row => row.join("")).join("\n"));
    }
}