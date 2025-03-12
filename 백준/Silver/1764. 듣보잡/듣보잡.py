import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name_set = set(input().strip() for _ in range(n))
result_list = []
for i in range(m):
    check_name = input().strip()
    if check_name in name_set:
        result_list.append(check_name)
print(len(result_list))
result_list.sort()
for i in result_list:
    print(i)