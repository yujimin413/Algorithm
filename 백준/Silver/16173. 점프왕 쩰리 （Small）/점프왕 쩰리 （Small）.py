import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())

grid = [[0] * n for _ in range(n)] # 맵
queue = deque()
dx = [0, 1]
dy = [1, 0]
visited = [[False] * n for _ in range(n)] # 방문 여부

for i in range(n):
    grid[i] = list(map(int, input().split()))

queue.append((0, 0))
visited[0][0] = True

while queue:
    now_x = queue[0][0]
    now_y = queue[0][1]
    queue.popleft()
    num = grid[now_x][now_y] # 이동 횟수
    for i in range(2):
        next_x = now_x + dx[i] * num
        next_y = now_y + dy[i] * num
        
        if next_x >= n or next_y >= n or next_x < 0 or next_y < 0:
            continue
        if visited[next_x][next_y] == True:
            continue
        if grid[next_x][next_y] == -1:
            print("HaruHaru")
            exit()
        queue.append((next_x, next_y))
        visited[next_x][next_y] = True
        
print("Hing")
        