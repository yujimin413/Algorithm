import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
deque = deque()
for _ in range(n):
    cmd = input().split()
    # print(cmd)
    if cmd[0] == 'push_front':
        deque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(deque) != 0:
            print(deque[0])
            deque.popleft()
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(deque) != 0:
            print(deque[len(deque) - 1])
            deque.pop()
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(deque) != 0:
            print(deque[len(deque) - 1])
        else:
            print(-1)
