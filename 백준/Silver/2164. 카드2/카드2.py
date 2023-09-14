import sys
from collections import deque


n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    queue.append(i+1)   # 1, 2, 3, 4

while len(queue)>1:
    queue.popleft()     #가장왼쪽값 읽은 후 -> 삭제(pop)  
    queue.append(queue.popleft())   #가장왼쪽값 append(뒤로 보내기)
    
print(queue.pop())