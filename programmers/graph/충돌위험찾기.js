function solution(points, routes) {
    var answer = 0;
    const map = new Map();
    
    for (const route of routes) {
        let [cur_row, cur_col] = points[route[0] - 1];
        let time = 0;
        const key = [cur_row, cur_col, time].toString(); 
        map.set(key, (map.get(key) || 0) + 1);
        
        for (let i = 1; i < route.length; i++) {
            const [next_row, next_col] = points[route[i] - 1];
            
            while (cur_row !== next_row) {
                if (cur_row < next_row) cur_row++;
                else cur_row--;
                const key = [cur_row, cur_col, ++time].toString();
                map.set(key, (map.get(key) || 0) + 1);
            }
            
            while (cur_col !== next_col) {
                if (cur_col < next_col) cur_col++;
                else cur_col--;
                const key = [cur_row, cur_col, ++time].toString();
                map.set(key, (map.get(key) || 0) + 1);
            }
        }
    }
    for (const v of map.values()) {
        if (v > 1) answer++;
    }

    return answer;
}