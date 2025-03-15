import sys
import heapq
input = sys.stdin.readline
n = int(input())
worker = dict()
for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        worker[name] = status
    if status == 'leave':
        del worker[name]
worker = sorted(worker.keys(), reverse = True)
for key in worker:
    print(key)

