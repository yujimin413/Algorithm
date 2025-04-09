import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # dfs 재귀호출 충분히늘려두기

n = int(input().strip())
arr = list(map(int, input().split()))
start = int(input().strip()) - 1
visited = [False] * n
visited[start] = True

def dfs(now):
    global visited
    for next in (now - arr[now], now + arr[now]):
        if 0 <= next < n and visited[next] == False:    
            visited[next] = True
            dfs(next)

dfs(start)
print(visited.count(True))
