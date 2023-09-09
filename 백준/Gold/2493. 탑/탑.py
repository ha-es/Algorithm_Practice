import sys
input = sys.stdin.readline    #반복문으로 여러줄 입력받는 상황

n = int(input()) 

tower = list(map(int,input().split()))
stack = []    #[ (탑의 인덱스), (탑의 높이) ]
result = []

for i in range(n):
    while stack:
        if stack[-1][1] >= tower[i]: # 수신할 탑 존재
            result.append(stack[-1][0]+1) # 인덱스 값 + 1 해줘야 수신할 탑의 번호가 됨
            break
        else: stack.pop()

    if not stack:
        result.append(0) # 스택이 비어있으면 수신할 탑이 없으므로 0
    
    stack.append((i, tower[i])) # 탑의 인덱스와 높이는 일단 stack에 집어 넣어야 함 

for i in result:
    print(i, end = ' ')
