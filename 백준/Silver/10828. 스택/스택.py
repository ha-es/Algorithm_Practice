# 스택
# push - pop
# 가장 마지막에 삽입된 자료가 가장 먼저 삭제
# top으로 정한곳을 통해서만 접근 가능
# 삽입 연산 -> push
# 삭제 연산 -> pop

import sys
n = int(sys.stdin.readline())

stack=[]

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        stack.append(command[1])
        
    elif command[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
            
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])    # pop()을해서 계속 틀렸음