import sys
input = sys.stdin.readline

txt = list(input().rstrip()) # 입력 먼저 받기 
dat = [-1] * 600001
pre = [-1] * 600001
nxt = [-1] * 600001

for i in range(len(txt) + 1):
    if i == 0: 
        dat[i] = -1
        pre[i] = -1
    else:
        dat[i] = txt[i - 1]
        pre[i] = i - 1
    if i == len(txt): 
        nxt[i] = -1
    else:
        nxt[i] = i + 1

n = int(input()) 
cur = len(txt)
unused = len(txt) + 1
length = len(txt)

for i in range(n):
    parts = input().split()
    cmd = parts[0]
    if cmd == 'L' and pre[cur] != -1:
        cur = pre[cur]
    elif cmd == 'D' and nxt[cur] != -1:
        cur = nxt[cur]
    elif cmd == 'B' and pre[cur] != -1:
        nxt[pre[cur]] = nxt[cur]
        pre[nxt[cur]] = pre[cur]
        cur = pre[cur]
        length -= 1
    elif 'P' in cmd:
        word = parts[1]
        dat[unused] = word
        pre[unused] = cur
        if nxt[cur] == -1:
            nxt[cur] = unused
        else:
            nxt[unused] = nxt[cur]
            pre[nxt[unused]] = unused
            nxt[pre[unused]] = unused
            
        cur = nxt[cur]
        
        unused += 1    
        length += 1  

cur = nxt[0]
while True:
    if pre[cur] == -1:
        cur = nxt[cur]
        continue
    print(dat[cur], end = '')
    if nxt[cur] == -1:
        break
    cur = nxt[cur]

