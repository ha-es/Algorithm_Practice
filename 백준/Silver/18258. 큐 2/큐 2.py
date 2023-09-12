import sys

n = int(sys.stdin.readline())

queue=[]
cnt=0   #가장 앞을 가르키는 인덱스 값

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        if len(queue)-cnt==0:
            print(-1)        
        else:
            print(queue[cnt])   #cnt에 해당되는 부분출력
            cnt+=1              #가장 앞쪽을 가르키는 인덱스를 그 다음 칸을 가르키도록
         
    elif command[0] == 'size':
        print(len(queue)-cnt)       #cnt만큼 빼줘야함
        
    elif command[0] == 'empty':
        if len(queue)-cnt==0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'front':
        if len(queue)-cnt==0:
            print(-1)
        else:
            print(queue[cnt]) 
            
    elif command[0]=='back':
        if len(queue)-cnt==0:
            print(-1)
        else:
            print(queue[-1])