import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
poketmon_dict = {}

for i in range(n):
    poketmon_dict.update({i + 1 : input().strip()})
    
poketmon_dict_reverse = {v : k for k, v in poketmon_dict.items()}
# print(poketmon_dict)
# print(poketmon_dict_reverse)

for _ in range(m):
    cmd = input().strip()
    if (cmd[0] >= 'A' and cmd[0] <= 'Z') or (cmd[0] >= 'a' and cmd[0] <= 'z'):
        print(poketmon_dict_reverse[cmd])
    else:
        print(poketmon_dict[int(cmd)])
    