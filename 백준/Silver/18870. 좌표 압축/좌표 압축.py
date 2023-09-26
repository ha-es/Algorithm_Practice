import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(x))        # 중복제거를 위해 set형으로 변환

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i
    
for i in x:
    print(dic[i], end=' ')