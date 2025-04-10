import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    adj_list = [[] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(n):
        adj_list[i + 1].append(arr[i])
    ans = 0
    for start in arr:
        if visited[start] == True:
            continue
        queue = deque()        
        queue.append((start))
        visited[start] = True

        while (queue):
            now = queue.popleft()
            for next in adj_list[now]:
                if next == start:
                    ans += 1
                if visited[next] == True:
                    continue
                queue.append(next)
                visited[next] = True
            
    print(ans)
