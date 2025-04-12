import sys
from collections import deque
input = sys.stdin.readline
str = input().strip()
n = int(input().strip())
ring_list = []
ans = 0
for i in range(n):
    ring = input().strip()
    ring_list.append(ring)
    
    for _ in range(10):
        if str in ring_list[i]:
            ans += 1
            break
        ring = deque(ring_list[i])
        ring.rotate(1)
        ring_list[i] = ''.join(ring)
print(ans)