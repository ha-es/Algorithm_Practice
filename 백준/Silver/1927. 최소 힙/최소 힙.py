import sys
import heapq

n = int(sys.stdin.readline())
heap =[]

for i in range(n):
    m = int(sys.stdin.readline())
    
    if m==0:
        if len(heap):
            print(heapq.heappop(heap))   
        else:
            print(0)   
    else:
        heapq.heappush(heap, m)