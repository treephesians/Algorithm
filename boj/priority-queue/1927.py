import heapq
import sys
N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        if not heap:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)