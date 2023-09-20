n= int(input())

def hanoi(x,y,z,n):
    if n==1:
        print(x,z)
        
    else:
        hanoi(x,z,y,n-1)
        print(x,z)
        hanoi(y,x,z,n-1)
    
print(2**n-1)

hanoi(1,2,3,n)