from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
# print(tmp)
# print(len(tmp))
# exit()
stack = deque()
for _ in range(n):
    tmp = input().split()
    if len(tmp) != 1: # 1 X 입력
        n, k = map(int, tmp)
        stack.append(k)
    else: # 2 or 3 or 4 or 5 입력
        n = int(tmp[0])
        if n == 2:
            if len(stack) != 0:
                print(stack[len(stack) - 1])
                stack.pop()
            else:
                print(-1)
        elif n == 3:
            print(len(stack))
        elif n == 4:
            if len(stack) != 0:
                print(0)
            else:
                print(1)
        elif n == 5:
            if len(stack) != 0:
                print(stack[len(stack) - 1])
            else:
                print(-1)
    