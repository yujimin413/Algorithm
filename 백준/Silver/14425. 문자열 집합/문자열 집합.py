import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s_list = list(input().strip() for _ in range(n))
cnt = 0
for j in range(m):
    check_str = input().strip()
    if check_str in s_list:
        cnt += 1
print(cnt)