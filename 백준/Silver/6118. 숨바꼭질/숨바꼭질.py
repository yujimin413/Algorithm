import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
visited_depth = [-1] * (n + 1) # -1 이면 방문 X, 0 아니면 depth 저장
for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
queue = deque()
visited_depth[1] = 0 # 시작 노드 1은 depth가 0
queue.append(1) # 현재노드
while(queue):
    now = queue.popleft()
    for next in adj_list[now]:
        if visited_depth[next] != -1:
            continue
        visited_depth[next] = visited_depth[now] + 1 # depth 저장
        queue.append(next)
max_depth = max(visited_depth)
print(visited_depth.index(max_depth), max_depth, visited_depth.count(max_depth))