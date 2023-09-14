import sys
from collections import deque

n, k = map(int, input().split())

q = deque()
r = []

for i in range(n):
    q.append(i+1)
    
while q:
    for i in range(k-1):
        q.append(q.popleft())
    r.append(q.popleft())

print('<', end='')

for i in range(len(r)):
    if i == len(r)-1:
        print(r[i], end='>')
        
    else:
        print(r[i], end=', ')
        
    
    
