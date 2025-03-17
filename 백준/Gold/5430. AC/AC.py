import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
arr = []

for _ in range(t):
    cmd = input().strip()
    n = int(input())
    arr = deque(eval(input())) # eval은 문자열로 표현된 표현식을 그대로 실행

    # 계산 줄이기
    cmd.replace('RR', '') # RR인 경우 원래와 같기 때문에 명령어 삭제
    if cmd.count('D') > len(arr): # 배열 원소 수보다 delete 많이하면 error
        print('error')
        continue

    error_flag = 0
    reverse_flag = 1 # 매번 reverse하면 시간 복잡도 증가하므로 flag처리
    for i in range(len(cmd)):
        if cmd[i] == 'R':
            reverse_flag *= -1
        elif cmd[i] == 'D':
            if len(arr) == 0:
                print('error')
                error_flag = 1
                break
            elif reverse_flag == 1: # 정방향이면 앞에서 pop
                arr.popleft() # 리스트는 슬라이싱 -> O(N), 덱은 O(1)이므로 덱 사용
            elif reverse_flag == -1: # 역방향이면 뒤에서 pop
                arr.pop()
    if error_flag == 1:
        continue
    if reverse_flag == -1: # -1일 떼만 reverse 실행
        arr.reverse()
    print(str(list(arr)).replace(' ', ''))
