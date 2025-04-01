import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())

adjmatrix = [[0] for _ in range(n + 1)] # 인접 그래프
queue = deque()
visited = [False] * (n + 1) # 방문 여부
ans = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    adjmatrix[u].append(v)
    adjmatrix[v].append(u)

for i in range(1, n + 1):
    adjmatrix[i] = sorted(adjmatrix[i], reverse = True)

queue.append(r)
visited[r] = True
ans[r] = 1

order = 1
while queue:
    now = queue.popleft()
    for next in adjmatrix[now]:
        if next == 0:
            continue
        if visited[next] == True:
            continue
        
        queue.append(next)
        order += 1
        visited[next] = True
        ans[next] = order
for i in ans[1 : n + 1]:
    print(i)
        
       

