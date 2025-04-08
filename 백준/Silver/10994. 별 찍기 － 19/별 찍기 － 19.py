import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
size = n * 4 - 3
ans = [[' '] * (size) for _ in range(size)]
# print(ans)
# exit()

def star(x, y, length):
    ans[x][y : y + length] = ['*'] * length # 윗 줄 가로
    ans[x + length - 1][y : y + length] = ['*'] * length # 아랫 줄 가로
    for row in range(x + 1, x + length - 1):
        ans[row][y] = '*' # 왼쪽 줄 세로
        ans[row][y + length - 1] = '*' # 오른쪽 줄 세로

curr_size = size
x = 0
y = 0
while(curr_size >= 1):
    star(x, y, curr_size)
    curr_size -= 4
    x += 2
    y += 2


for i in range(size):
    for length in range(size):
        print(ans[i][length], end = '')
    print()

