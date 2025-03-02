function solution(begin, target, words) {
    var answer = Infinity;

    function check(begin, word){
        let result = 0;
        const len = word.length
        for (let i = 0; i < len; i++){
            if (begin[i] === word[i]) result++;
        }
        if (result == len - 1) return true;
        return false;

    }

    function backtracking(begin, words, count){
        if (begin === target){
            answer = Math.min(answer, count);
            return;
        }
        for (let i = 0; i < words.length; i++){
            if (check(begin, words[i])){
                const new_words = [...words];
                new_words.splice(i, 1);
                backtracking(words[i], new_words, count + 1);
            }
        }
    }

    backtracking(begin, words, 0);
    if (answer == Infinity) answer = 0;

    return answer;
}

const begin = "hit";
const target = "cog";
const words = ["hot", "dot", "dog", "lot", "log", "cog"];

console.log(solution(begin, target, words));