function check_name(user_id, banned_id) {
    if (user_id.length !== banned_id.length) return false;
    for (let i = 0; i < user_id.length; i++) {
        if (banned_id[i] === '*') continue;
        if (user_id[i] !== banned_id[i]) return false;
    }
    return true;
}

function solution(user_id, banned_id) {
    const uniqueCombinations = new Set(); // 중복 제거를 위한 Set
    const n = banned_id.length;

    function backtracking(selected_id, used) {
        if (selected_id.length === n) {
            // 중복 방지를 위해 정렬 후 문자열 변환하여 Set에 추가
            const sortedKey = [...selected_id].sort().join(",");
            uniqueCombinations.add(sortedKey);
            return;
        }

        for (let i = 0; i < user_id.length; i++) {
            if (used[i]) continue; // 이미 선택한 아이디는 스킵

            const currentBannedIdx = selected_id.length;
            if (check_name(user_id[i], banned_id[currentBannedIdx])) {
                used[i] = true;
                selected_id.push(user_id[i]);

                backtracking(selected_id, used);

                selected_id.pop();
                used[i] = false;
            }
        }
    }

    backtracking([], Array(user_id.length).fill(false));
    return uniqueCombinations.size;
}

// 예제 실행
const user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"];
const banned_id = ["*rodo", "*rodo", "******"];
console.log(solution(user_id, banned_id)); // ✅ 정답: 2