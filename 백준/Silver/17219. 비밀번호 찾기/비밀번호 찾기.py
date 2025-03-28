import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dict = dict()

for domain in range(n):
    list = input().split()
    domain = list[0]
    dict[domain] = list[1]

for _ in range(m):
    print(dict[input().strip()])