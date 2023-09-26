import sys
n= list(map(int, input().split()))
m =[]

# 항상 5개니까 while문을 사용
while True:
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            temp = n[i]
            n[i]= n[i+1]
            n[i+1]=temp
            print(' '.join(map(str, n)))
    if n == [1, 2, 3, 4, 5]:
        break