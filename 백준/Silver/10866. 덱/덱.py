import sys
from collections import deque

n = int(sys.stdin.readline())

s = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0]=='push_front':
        s.appendleft(command[1])
    
    elif command[0]=='push_back':
        s.append(command[1])
    
    elif command[0]=='pop_front':
        if len(s)!=0:
            print(s.popleft())
        else:
            print(-1)
            
    elif command[0]=='pop_back':
        if len(s)!=0:
            print(s.pop())
        else:
            print(-1)
            
    elif command[0]=='size':
        print(len(s))
        
    elif command[0]=='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
            
    elif command[0]=='front':
        if len(s)!=0:
            print(s[0])
        else:
            print(-1)
            
    elif command[0]=='back':
        if len(s)!=0:
            print(s[-1])
        else:
            print(-1)