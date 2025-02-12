function solution(brown, yellow) {
    for (let i = parseInt(Math.sqrt(yellow,2)); 1 <= i ; i--){
        if (yellow % i == 0){
            const row = i, col = yellow / i;
            if ( (row + col + 2) * 2 == brown )
                return [col + 2, row + 2]
        }
    }
}

console.log(solution(8, 1))