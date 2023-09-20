n = int(input())
cpaper=[]
blue_cnt, white_cnt = 0, 0

for _ in range(n):
    row = list(map(int, input().rsplit()))
    cpaper.append(row)


def check(row, col, n):
    global blue_cnt, white_cnt

    curr = cpaper[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if curr != cpaper[i][j]:
                n_paper = n//2

                check(row, col, n_paper) #1
                check(row, col+n_paper, n_paper) #2
                check(row+n_paper, col, n_paper) #3
                check(row+n_paper, col+n_paper, n_paper) #4
                return
    if curr==0:
        white_cnt +=1
    else:
        blue_cnt +=1
    return


check(0,0,n)
print(white_cnt)
print(blue_cnt)