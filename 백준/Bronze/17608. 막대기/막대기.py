import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
h_list = list(int(input().strip()) for _ in range(n))
cnt = 0
highest = 0
for i in range(n - 1, -1, -1):
    if h_list[i] > highest:
        highest = h_list[i]
        cnt += 1
print(cnt)