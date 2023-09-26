import sys

n = int(sys.stdin.readline())
m = []

for i in range(n):
    age, name =input().split()
    m.append([int(age), name])
    
for i in sorted(m, key=lambda x : x[0]):
    print(i[0],i[1])