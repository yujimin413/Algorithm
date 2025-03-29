import sys

input = sys.stdin.readline
x = int(input().strip())
n = int(input().strip())

sum = 0
for _ in range(n):
    list = input().split()
    cost = int(list[0])
    cnt = int(list[1])
    sum += cost * cnt
if x == sum:
    print("Yes")
else:
    print("No")