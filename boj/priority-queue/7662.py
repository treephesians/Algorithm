import sys
import heapq

def process_operations(ops):
    min_heap = []
    max_heap = []
    visited = [False] * len(ops)
    idx = 0  # unique ID for each insertion

    for op, num in ops:
        if op == 'I':
            # insert num with ID idx
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1
        else:  # 'D'
            if num == 1:
                # delete max
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, id_max = heapq.heappop(max_heap)
                    visited[id_max] = False
            else:  # num == -1
                # delete min
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, id_min = heapq.heappop(min_heap)
                    visited[id_min] = False

    # clean up both heaps
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap:
        return "EMPTY"
    else:
        maximum = -max_heap[0][0]
        minimum = min_heap[0][0]
        return f"{maximum} {minimum}"

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        k = int(input())
        ops = []
        for _ in range(k):
            line = input().split()
            ops.append((line[0], int(line[1])))
        print(process_operations(ops))

if __name__ == "__main__":
    main()