import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
deque = deque(range(1, n + 1))

pop_num_list = list(map(int, input().split()))

cnt = 0
for pop_num in pop_num_list:
    pop_idx = 0
    for idx in range(len(deque)):
        if deque[idx] == pop_num:
            pop_idx = idx
            break

    if pop_idx > len(deque) / 2: # right_rotate
        while deque[0] != pop_num:
            deque.rotate(1)
            cnt += 1
        deque.popleft()
    else:                  # left_rotate
        while deque[0] != pop_num:
            deque.rotate(-1)
            cnt += 1    
        deque.popleft()
print(cnt)