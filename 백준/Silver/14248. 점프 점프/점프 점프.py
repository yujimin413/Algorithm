import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
start = int(input().strip()) - 1
av_dist = arr[start - 1]
queue = deque()
visited = [False ] * n
queue.append((start, arr[start])) # 시작지점, 가능한 이동 거리
visited[start] = True

while (queue):
    now, av_dist = queue.popleft()
    for next in (now - arr[now], now + arr[now]):
        if 0 <= next < n and visited[next] == False:    
            queue.append((next, arr[next]))
            visited[next] = True
print(visited.count(True))