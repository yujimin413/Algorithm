from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
queue = deque(range(1, n + 1))
print('<', end = '')
while (len(queue) != 0):
    queue.rotate(-(k - 1))
    print(queue[0], end = '')
    queue.popleft()
    if len(queue) != 0:
        print(', ', end = '')
print('>')