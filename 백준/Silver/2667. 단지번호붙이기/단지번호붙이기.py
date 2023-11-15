#지도의 크기
n = int(input())

graph=[]
num=[]


#단지 지도 만들기
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [0,0,1,-1]
dy = [-1,1,0,0]



def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    # 1이라면
    #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
    if graph[x][y]==1:
        global cnt
        cnt+=1
        graph[x][y]=0
        
        # 상하좌우 재귀
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False


cnt = 0
result = 0


for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            num.append(cnt)
            result+=1
            cnt=0
num.sort()
print(result)

for i in range(len(num)):
    print(num[i])
            