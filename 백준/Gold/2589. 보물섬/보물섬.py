from collections  import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph=[]

for _ in range(N):
    graph.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
    
def bfs(x, y):
    q = deque()
    q.append((x,y))
    
    visited = [[0]*M for _ in range(N)]
    visited[x][y]=1
    cnt=0
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx <0 or nx >=N or ny<0 or ny >=M:
                continue
            elif graph[nx][ny]=='L' and visited[nx][ny]==0:
                visited[nx][ny]= visited[x][y]+1
                cnt= max(cnt, visited[nx][ny])
                q.append((nx,ny))               
    return cnt-1

result=0
for i in range(N):
    for j in range(M):
        if graph[i][j]=='L':
            result= max(result, bfs(i,j))
print(result)