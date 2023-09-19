import sys

n = int(input())
fibo=[0,1]

for i in range(2,n+1):
    num = fibo[i-1]+fibo[i-2]     #피보나치 f(2) = f(0) + f(1) ...
    fibo.append(num)
print(fibo[n])
