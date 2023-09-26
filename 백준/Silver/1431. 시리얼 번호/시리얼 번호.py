n = int(input())
s_list = []

for _ in range(n):
    s_num = list(input())
    sum = 0
    for i in s_num:
        if i.isdigit():
            sum+= int(i)
    s_list.append( (''.join(s_num),len(s_num),sum) )
s_list.sort(key=lambda x:(x[1],x[2],x[0]))

for i in s_list:
    print(i[0])