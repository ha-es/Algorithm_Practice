from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
count = [0 for _ in range(F+1)]

def bfs(): 
    global flag 
    q = deque()
    q.append(S)
    count[S]=1
    while q:
        cur = q.popleft()
        if cur == G: 
            flag = True
            print(count[cur]-1)
            break 
        for i in (U, -D):
            next = cur + i  
            if 1<=next<=F and count[next]==0:
                count[next] = count[cur] + 1 
                q.append(next) 
flag = False 
bfs()
if flag==False: 
    print("use the stairs") 