import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
deque = deque()
for _ in range(n):
    cmd = input().split()
    # print(cmd)
    if cmd[0] == '1':
        deque.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        deque.append(int(cmd[1]))
    elif cmd[0] == '3':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif cmd[0] == '4':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif cmd[0] == '5':
        print(len(deque))
    elif cmd[0] == '6':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == '7':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif cmd[0] == '8':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])
