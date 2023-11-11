# 컴퓨터 수
n= int(input())
# 노드의 수 ( 연결된 쌍의 개수 )
m= int(input())


graph =[[] for _ in range(n+1)]
visit = [False]* (n+1)
cnt=0

# 연결된 정점 입력
for i in range(m):
    x, y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(x):
    global cnt
    visit[x]=True
    for i in graph[x]:
        if not visit[i]:
            cnt+=1
            dfs(i)
            
dfs(1)
print(cnt)
            
