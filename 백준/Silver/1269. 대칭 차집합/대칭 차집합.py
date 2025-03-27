import sys

input = sys.stdin.readline
m, n = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_dict = {i: True for i in a} # 리스트의 원소를 키로 갖는 dict 생성
b_dict = {i: True for i in b}


cnt = m + n
for i in b:
    if i in a_dict:
        cnt -= 1
for i in a:
    if i in b_dict:
        cnt -= 1

print(cnt)