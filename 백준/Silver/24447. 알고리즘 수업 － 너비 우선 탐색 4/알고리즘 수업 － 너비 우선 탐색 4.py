import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())

adjmatrix = [[] for _ in range(n + 1)] # 인접 그래프
queue = deque()
visited = [False] * (n + 1) # 방문 여부

depth_list = [-1] * (n + 1)  # 방문 깊이
order_list = [0] * (n + 1) # 방문 순서

for i in range(m):
    u, v = map(int, input().split())
    adjmatrix[u].append(v)
    adjmatrix[v].append(u)

for i in range(1, n + 1):
    adjmatrix[i] = sorted(adjmatrix[i])

depth = 0
order = 1
queue.append((r, depth))
visited[r] = True
depth_list[r] = 0
order_list[r] = 1

while queue:
    now, depth = queue.popleft()
    for next in adjmatrix[now]:
        if visited[next] == True:
            continue
        queue.append((next, depth + 1))
        order += 1
        visited[next] = True
        depth_list[next] = depth + 1
        order_list[next] = order
ans = 0
for i in range(1, n + 1):
    ans += order_list[i] * depth_list[i]
print(ans)