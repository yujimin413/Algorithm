import sys
input = sys.stdin.readline
n = int(input())
card_list = set(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))
for i in check_list:
    if i in card_list: # set은 in 수행 시 O(1). list는 O(n)
        print(1, end = ' ')
    else:
        print(0, end = ' ')