n = int(input())


def hanoi(x, y, z, n):
    if n==1:
        print(x,z)         
    else:
        hanoi(x,z,y,n-1)  
        print(x,z)
        hanoi(y,x,z,n-1)  
    
print(2**n-1)             

# n이 20이하인 경우
if(n<=20):
    hanoi(1,2,3,n)