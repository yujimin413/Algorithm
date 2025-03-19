import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
card_list = deque()
for i in range(1, n + 1):
    card_list.append(i)

for _ in range(n):
    if len(card_list) != 0:
        print(card_list.popleft(), end = ' ')
        card_list.rotate(-1)