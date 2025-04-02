import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())

adjmatrix = [[] for _ in range(n + 1)] # 인접 그래프
queue = deque()
visited = [False] * (n + 1) # 방문 여부
ans = [-1] * (n + 1) # depth 저장

for i in range(m):
    u, v = map(int, input().split())
    adjmatrix[u].append(v)
    adjmatrix[v].append(u)

for i in range(1, n + 1):
    adjmatrix[i] = sorted(adjmatrix[i])

depth = 0
queue.append((r, depth))
visited[r] = True
ans[r] = 0

while queue:
    now, depth = queue.popleft()
    for next in adjmatrix[now]:
        if visited[next] == True:
            continue
        queue.append((next, depth + 1))
        visited[next] = True
        ans[next] = depth + 1
for i in ans[1 : n + 1]:
    print(i)
        
        



