import sys
input = sys.stdin.readline

n = int(input().rstrip())


for i in range(n):
    stack_l = []
    stack_r = []
    cmd = list(input().strip())
    for i in cmd:
        if i == '<':
            if not stack_l: continue
            stack_r.append(stack_l.pop())
        elif i == '>':
            if not stack_r: continue
            stack_l.append(stack_r.pop())
        elif i == '-':
            if not stack_l: continue
            stack_l.pop()
        else: # 문자 입력
            stack_l.append(i)
            
    stack_l.extend(reversed(stack_r))
    print(*stack_l, sep = '')

