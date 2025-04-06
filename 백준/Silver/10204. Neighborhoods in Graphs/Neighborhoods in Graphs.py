import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    str = input().split('v')

    v, e = map(int, str[0].split())

    e_list = list(map(int, str[1 : 2 * e + 1])) # index 2 부터 : index 1 + edges 쌍 개수 + 그 다음 index
    
    start_v = int(str[len(str) - 1])

    visited = [False] * (v + 1) # v + 1: index 1부터 사용
    depth_list = [0] * (v + 1)

    adj = [[] for _ in range(v + 1)]  # v + 1: index 1부터 사용
    for i in range(0, e * 2, 2): # 인접리스트

        v_1 = e_list[i]
        v_2 = e_list[i + 1]

        adj[v_1].append(v_2)
        adj[v_2].append(v_1)

    queue = deque()

    depth = 0
    visited[start_v] = True
    queue.append((start_v, depth)) # (vertix, depth)
    
    
    while (queue):
        now, depth = queue.popleft()

        for next in adj[now]:
            if visited[next] == True:
                continue
            # depth += 1
            visited[next] = True
            queue.append((next, depth + 1))
            depth_list[next] = depth + 1

    ans = 0
    for i in depth_list:
        if i >= 1 and i <= 2:
            ans += 1
    print(f'The number of supervillains in 2-hop neighborhood of v{start_v} is {ans}')