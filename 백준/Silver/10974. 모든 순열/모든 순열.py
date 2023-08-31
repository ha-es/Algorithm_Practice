n = int(input())

s =[]

def d():
    if n==0:
        return False
    if len(s)==n:
        print(*s)
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            d()
            s.pop()
            
d()