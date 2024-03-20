import sys

N = int(sys.stdin.readline())  # input()으로 변경
time_table = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())  # input()으로 변경
    time_table.append([start, end])

time_table.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간으로 먼저 정렬하고, 시작 시간으로 차선으로 정렬

last_end_time = 0
meetings = 0

for start, end in time_table:
    if start >= last_end_time:
        meetings += 1
        last_end_time = end

print(meetings)