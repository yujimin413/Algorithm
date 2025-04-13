import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [[] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dy = [-1, 1, 0, 0] # 상하좌우
dx = [0, 0, -1, 1]
queue = deque()

for i in range(r):
    line = list(input().strip()) # list(): 한 문자씩 나누기
    grid[i] = line
    indices = [idx for idx, char in enumerate(grid[i]) if char in ('v', 'o')]  # 모든 'v' or 'o'의 인덱스 추출
    for index in indices:
        queue.append((i,index))
survived_o = 0
survived_v = 0

while(queue):
    y, x = queue.popleft()
    if visited[y][x] == True:
        continue
    sub_queue = deque()
    sub_queue.append((y, x))
    visited[y][x] = True
    v_num = 0
    o_num = 0
    if grid[y][x] == 'v':
        v_num += 1
    elif grid[y][x] == 'o':
        o_num += 1
    while(sub_queue):
        now_y, now_x = sub_queue.popleft()
        visited[now_y][now_x] = True

        for i in range(4): # 상하좌우
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if 0 <= next_y < r and 0 <= next_x < c:
                if grid[next_y][next_x] == '#' or visited[next_y][next_x] == True:
                    continue
                if grid[next_y][next_x] == '.':
                    sub_queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
                if grid[next_y][next_x] == 'v':
                    v_num += 1
                    sub_queue.append((next_y, next_x))
                    visited[next_y][next_x] = True

                elif grid[next_y][next_x] == 'o':
                    sub_queue.append((next_y, next_x))
                    visited[next_y][next_x] = True
                    o_num += 1
    if v_num >= o_num:
        survived_v += v_num
    else:
        survived_o += o_num
print(survived_o, survived_v)



    
    