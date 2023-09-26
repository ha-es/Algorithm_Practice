n = int(input())
sort_list =[]

for i in range(n):
    sort_list.append(int(input()))      # sort_list.append(n)을 해서 오류..

sort_list = sorted(sort_list)           # 오름차순으로 정렬
for i in range(len(sort_list)):
    print(sort_list[i])