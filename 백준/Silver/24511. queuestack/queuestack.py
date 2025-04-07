import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
cmd_list = list(map(int, input().split())) # 0-queue, 1-stack
num_list = list(map(int, input().split()))

queue_stack = deque()
for i in range(n):
    if cmd_list[i] == 0: # stack은 영향 없으므로 무시
        queue_stack.append(num_list[i])

m = int(input().strip())
insert_list = list(map(int,input().split()))
for pop_x in insert_list:
    queue_stack.appendleft(pop_x)
    print(queue_stack.pop(), end=' ')