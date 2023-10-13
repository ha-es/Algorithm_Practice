import sys
n = int(input())
s = [0]*n

for x in range(n):
    s[x] = list(map(int, sys.stdin.readline().split()))
    

for i in range(1,n):
    for j in range(len(s[i])):
        if j == 0 :
            s[i][j] +=s[i-1][j]
        elif j==len(s[i])-1:
            s[i][j] +=s[i-1][j-1]
        elif j < len(s[i-1]):
            s[i][j] += max(s[i-1][j], s[i-1][j-1])
            
print(max(s[n-1]))